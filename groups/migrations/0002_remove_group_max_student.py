# Generated by Django 2.1 on 2018-09-04 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='max_student',
        ),
    ]