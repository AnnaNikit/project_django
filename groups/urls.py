from django.contrib import admin
from django.urls import path, re_path
from groups.views import all_groups, AddGroupView

urlpatterns = [
    path('all', all_groups),
    path('add', AddGroupView.as_view()),
]
