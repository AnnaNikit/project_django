from django.shortcuts import render,  redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views import View
from timetable.models import TimeTable, Attendance
from students.models import Student
from groups.models import Group
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.http import Http404, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import datetime
import json

def get_timetable_for_period(start_date, finish_date, group = None,days = None,time = None):
    if group == None or days == None or time == None:
            timetable = TimeTable.objects.extra(where=['start_date<=%s',
                'finish_date>=%s OR finish_date is NULL'],
                 params=[start_date, finish_date], order_by = ['days'])
    else:
            timetable = TimeTable.objects.extra(where=['start_date<=%s',
                    'finish_date>=%s OR finish_date is NULL'],
                     params=[start_date, finish_date]).filter(group = group,
                     days = days, time = time).get()
    return timetable

class ShowTimetableView(View):

    def get(self, request):
        today = datetime.date.today()
        monday = today - datetime.timedelta(days=today.weekday())
        mon = monday.strftime("%Y-%m-%d")
        query = get_timetable_for_period(mon,mon)
        sun = monday+datetime.timedelta(days=6)
        dict_timetabl = {}
        for item in query:
            dayweek   = monday+datetime.timedelta(days=item.days)
            item.total = Attendance.objects.filter(day = dayweek, lessons = item).count()
            item.days = dayweek.strftime("%A")
            dayweek   = dayweek.strftime("%a,%d %b %Y")
            if dayweek in dict_timetabl:
               dict_timetabl[dayweek].append(item)
            else:
               dict_timetabl[dayweek] = [item]
        p = {'timetable_dict': dict_timetabl,
             'mon':monday.strftime("%#d %b %y"),
             'sun':sun.strftime("%#d %b %y"), }
        return HttpResponse(render(request, 'show-timetable.html',p))

def sign_up(request):

    if request.is_ajax():
        dict_request = request.GET.dict()
        lessons = dict_request["lessons"]
        day     = dict_request["day"]
        name    = dict_request["name"]
        email   = dict_request["email"]
        time    = dict_request["time"]
        group = Group.objects.get(name = lessons)
        days =  datetime.datetime.strptime(day, "%a,%d %b %Y")

        today = datetime.date.today()
        monday = today - datetime.timedelta(days=today.weekday())
        mon = monday.strftime("%Y-%m-%d")
        timetable = get_timetable_for_period (mon, mon, group, days.weekday(), time)
        # get or create student
        student = Student.objects.get_or_create(email = email,defaults={'name': name,'start_date':today},)
        student = student[0]

        # add  student in attendance
        stud_singup = Attendance.objects.filter(day = days, lessons = timetable, student = student).count()
        total       = Attendance.objects.filter(day = days, lessons = timetable).count()
        if stud_singup >=1:
            response = {'massege':'You have already signed up',
                        'total':total,
                        'max':timetable.max_student}
        elif total >= timetable.max_student:
            response = {'massege':'Sign up is over',
                        'total':total,
                        'max':timetable.max_student}
        else:
            attendance = Attendance()
            attendance.day      = days
            attendance.lessons  = timetable
            attendance.student  = student
            attendance.save()
            response = {'massege':'You sign up for lessons',
                        'total':total+1,
                        'max':timetable.max_student}
        return JsonResponse(response)
    else:
         raise Http404
