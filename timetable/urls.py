from django.contrib import admin
from django.urls import path, re_path
from timetable.views import ShowTimetableView
from . import views
urlpatterns = [
    path('timetable', ShowTimetableView.as_view()),
    path('SignUp/', views.sing_up),



]
