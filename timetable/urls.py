from django.contrib import admin
from django.urls import path, re_path
from timetable.views import ShowTimetableView

urlpatterns = [
    path('timetable', ShowTimetableView.as_view()),
]
