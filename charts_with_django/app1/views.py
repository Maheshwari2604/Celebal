# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Count , Q
from django.shortcuts import render, HttpResponse
from .models import Passenger
from django.template import RequestContext
# Create your views here.

def passenger1(request):
    dataset = Passenger.objects.values('AClass').annotate(sc=Count('AClass' , filter = Q(s=True)),
    nsc=Count('AClass' , filter = Q(s=False))).order_by('AClass')
    return render(request , 'app1/passenger_graph.html' , {'dataset' : dataset})

def passenger(request):
    dataset = Passenger.objects.values('AClass').annotate(sc=Count('AClass' , filter = Q(s=True)),
    nsc=Count('AClass' , filter = Q(s=False))).order_by('AClass')
    return render(request , 'app1/main.html', {'dataset' : dataset})

def login(request):
        print("in try")
        if request.method == 'POST':
            print "register in post"
            name = request.POST['name']
            AClass = request.POST['class']
            user = Passenger()
            user.name = name
            user.age = 11
            print(user.name)
            user.AClass = AClass
            print(user.AClass)
            completed = request.POST.get('completed')
            print(completed)
            if completed == None:
                user.s = False
            else:
                user.s = True
            
            user.save()
            dataset = Passenger.objects.values('AClass').annotate(sc=Count('AClass' , filter = Q(s=True)),
            nsc=Count('AClass' , filter = Q(s=False))).order_by('AClass')            
            return render(request,'app1/main.html', {'dataset': dataset})
        else:
            return HttpResponse("Exist, please try new one")