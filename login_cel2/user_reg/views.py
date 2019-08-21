# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import userprofile
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import hashlib

# Create your views here.
def user_signup(request):
    try:
        print("in try")
        if request.method == 'POST':
            print "register in post"
            #form = SignupForm(request.POST or None)
            #if form.is_valid():
            #password = form.cleaned_data['password']
            password = request.POST['password']
            print password
            password = hashlib.sha256(password.encode())
            password = password.hexdigest()
            #form.password = make_password(password)
            #pswd = form.password
            #print pswd
            #user = form.save(commit=False)
            #user.is_active = False
            #user.save()
            #userobj = form.cleaned_data
            #username = userobj['username']
            #email = userobj['email']
            #raw_password = userobj['password']
            user = userprofile()
            username = request.POST['first_name']
            email = request.POST['email']
            user.firstname = request.POST['first_name']
            user.password = password
            #user.password = make_password(password)    
            user.email = email    
            if not (userprofile.objects.filter(firstname=username).exists() or userprofile.objects.filter(email=email).exists()):
                #user.password = make_password(password)
                pd = user.password
                print "encrpted passwd is"
                print pd
                user.save()
                context = {
                    "message": "Activation link is sent to an email, Please activate your account"
                }
                return render(request, 'login_cel2/register.html', context)
            else:
                context = {
                'message': "Username or email exist please try something different"
            }
                return render(request,'login_cel2/register.html', context)
        else:
                return HttpResponse("Exist, please try new one")

    except:
        return HttpResponse("error in code")

def user_login(request):
    #context = {}
    #csrfContext = RequestContext(request)
    try:
        if request.method == 'POST':
            #con = {}
            username = request.POST['email']
            password = request.POST['password']

            password = hashlib.sha256(password.encode())
            password = password.hexdigest()
            #return HttpResponse(password)
            #user = register.objects.get(username=username)
            #return HttpResponse(user.password)
            try:
                passw = register_model.objects.get(username=username)
                passwordd = passw.password
                print (passw.password)
            
            except:
                print "error"

                
            #passwd = check_password(password, passwordd)
            #print (passwd)

            if password == passwordd:
                #user = authenticate(username = username, password = password)
                user = register_model.objects.get(username=username , password = passwordd)
            else:
                print("password not matched")
            #    print "error"
            #return HttpResponse(user)
            #return HttpResponse(user.username)
            if user:
                print(user)
                #return HttpResponse(user.id)
                #request.session['signupp_id'] = user
                print (user.id)
                request.session['user_id'] = user.id
                new_id = user.id
                user.save()
                print new_id
                #print (request.session['user_id'])
                #return render(request,'S_W/error.html',{'username':username})
                #login(request, user)
                #uu = request.session['signupp_id']
                #return HttpResponse(uu)
                #request.session['email_confirmed'] = True 

                return HttpResponseRedirect(reverse('home'))
            #else:
                #context['error'] = "Error in Connection"
                #return render(request, 'S_W/error.html', context)
        else:
            #context[error] = "ERROR"
            #return HttpResponse("eeeoooorrrrooror")
            return render(request, 'login_cel2/login.html')
    except:
        print "error3"
        context = {
            "message": "You are a new user, please register your account"
        }
        return render(request, 'login_cel2/login.html', context)

def home(request):
    print("hey")
    return HttpResponse ("Home")