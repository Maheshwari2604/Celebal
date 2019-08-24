# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def azure_login(request):
    print('hey')
    try:
        print(" u r in")
        return render(request , 'app1/home.html')
    except:
        print('u r out')

@login_required
def login_successful(request):
    return render(request, 'app1/login-successful.html')