from django.shortcuts import render,  redirect
from django.http import HttpResponse, HttpRequest
from django.views import View
from groups.models import Group
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

def all_groups(request):
    print(Group.objects.all())
    return HttpResponse(render(request, 'all_groups.html', {'groups': Group.objects.all()}))

class AddGroupView(View):
    def get(self, request):
        return HttpResponse(render(request, 'add-group.html'))

    def post(self, request):
        name = request.POST.get('name')
        
        group = Group()

        group.name = name
        group.start_date = start_date
        group.max_students = max_students

        group.save()
        print(group)

        return redirect('/groups/all')
