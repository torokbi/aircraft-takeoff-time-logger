from datetime import datetime, timedelta
from pickle import TRUE
from time import strftime
from turtle import st
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import plane

'''
The time_update is refersh the beforenext_takeoff columm in every minutes. 
'''
def time_update():
    planes = plane.objects.all()
    for aircrafts in planes:
        craft = plane.objects.get(pk = aircrafts.id)
        time = strftime("%H:%M")
        time_takeoff = timedelta(hours=int(str(aircrafts.takeofftime)[:2]), minutes=int(str(aircrafts.takeofftime)[3:5]))
        time_now = timedelta(hours=int(str(time)[:2]), minutes=int(str(time)[3:5]))
        before = time_now - time_takeoff
        if int(str(before)[2:4]) <= 45 :
            before = 45 - int(str(before)[2:4])
            craft.beforenext_takeoff = before
            craft.save()

'''
The reset is clear database at 22:00 every day.
'''
def reset ():
    plane.objects.all().delete()