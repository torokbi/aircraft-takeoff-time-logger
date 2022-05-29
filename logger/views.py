from datetime import datetime, timedelta
from multiprocessing import context
from pickle import TRUE
from time import strftime
from turtle import st
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import plane

# Create your views here.

def main(request):
    planes = plane.objects.all()
    find = False
    context = {}
    context['planes'] = planes
    next_time = 45

    if request.method == "POST":
        reg = request.POST.get('registration')
        time = strftime("%H:%M")
        for index in planes:
            if index.registration == reg:
                find = True
                context['error'] = f"A {reg} lajstromjelű repülőgép már egyszer rögzítésre került."
                return render(request, "main.html", context)
        if not find:
            planes = plane(registration=reg, takeofftime=time, beforenext_takeoff=next_time)
            planes.save()
            return redirect('mainpadge')
 
    return render(request, "main.html", context)

def howto(request):
    return render(request, "howto.html")

def about(request):
    return render(request, "about.html")

def retakeoff(request, id):
    craft = plane.objects.get(pk = id)
    next_time = 45
    time = strftime("%H:%M")
    craft.beforenext_takeoff = next_time
    craft.takeofftime = time
    craft.save()
    return redirect('mainpadge')

def delete_all_data(request):
    plane.objects.all().delete()
    return redirect('mainpadge')

def delete_one_plane(request, id):
    craft = plane.objects.get(pk = id)
    craft.delete()
    return redirect('mainpadge')