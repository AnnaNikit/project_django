from django.db import models
from groups.models import Group
from students.models import Student
import calendar

class TimeTable(models.Model):
    DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),)

    group       = models.ForeignKey(Group, on_delete=models.CASCADE, null=False)
    max_student = models.IntegerField()
    start_date  = models.DateField()
    finish_date = models.DateField(blank=True, null=True)
    days        = models.IntegerField(choices=DAYS_OF_WEEK)
    time        = models.TimeField()

    def __str__(self):
        return '%s %s %s %s'%(self.group, self.DAYS_OF_WEEK[self.days][1] , self.time, self.start_date )

class Attendance(models.Model):
    day     = models.DateField()
    lessons = models.ManyToManyField(TimeTable)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return '%s %s %s'%(self.day,self.lessons, self.student)
