from django.shortcuts import render,  redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views import View
from timetable.models import TimeTable, Attendance
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

import datetime
import json

from django.http import Http404, JsonResponse




class ShowTimetableView(View):
    DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),)

    def get(self, request):
        print(request.is_ajax())
        
        today = datetime.date.today()
        monday = today - datetime.timedelta(days=today.weekday())
        mon = monday.strftime("%Y-%m-%d")
        query = TimeTable.objects.extra(where=['start_date<=%s', 'finish_date>=%s OR finish_date is NULL'],
                 params=[mon, mon])

        dict_timetabl = {}
        for item in query:
            print(10000000000000)
            dayweek   = monday+datetime.timedelta(days=item.days)
            item.total = Attendance.objects.filter(day = dayweek, lessons = item).count()
            dayweek   = dayweek.strftime("%A,%d %b %Y")
            item.days = self.DAYS_OF_WEEK[item.days][1]
            if dayweek in dict_timetabl:
               dict_timetabl[dayweek].append(item)
            else:
               dict_timetabl[dayweek] = [item]
        p = {'timetable_dict': dict_timetabl}

        return HttpResponse(render(request, 'show-timetable.html',p))

    def post(self, request):
        print(request.is_ajax())

        if request.is_ajax():
            test = 5
            print(10)
        return HttpResponse(json.dumps({'ss':4}),content_type="application/json")

from django.http import Http404, JsonResponse


def add_ajax(request):
    if request.is_ajax():
        response = {'first-text': 'Lorem Ipsum is simply dummy text', 'second-text': 'to make a type specimen book. It has '}

        return JsonResponse(response)
    else:
        raise Http404
