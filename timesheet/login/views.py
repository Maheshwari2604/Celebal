# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from dbo.models import Employee
from django.shortcuts import render , HttpResponse , reverse , HttpResponseRedirect
from django.template import RequestContext

# Create your views here.
def user_login(request):
    #context = {}
    #csrfContext = RequestContext(request)
    # print('in try')
    # try:
        print('in try')
        if request.method == 'POST':
            print('in post')
            #con = {}
            username = request.POST['email']
            print(username)
            password = request.POST['password']
            print(password)
            #return HttpResponse(password)
            #user = register.objects.get(username=username)
            #return HttpResponse(user.password)
            try:
                user = Employee.objects.get(emp_id=username)
                # pwd = hashlib.sha256(password.encode())
                # pwd = password.hexdigest()
                pwd = user.password
                print (user.password)
            
            except:
                print "error"

                
            #passwd = check_password(password, passwordd)
            print (user)
            #user = authenticate(username = username, password = password)
            if user:
                userr = Employee.objects.get(emp_id=username , password = pwd)
            else:
                return HttpResponse(user)

            if userr:
                print(userr)
                
                request.session['user_id'] = userr.id
                request.session['email'] = userr.emp_id
                #print(request.session['user_id'])
                new_id = user.id
                return HttpResponseRedirect(reverse('home'))
                #print (request.session['user_id'])
                #return render(request,'S_W/error.html',{'username':username})
                #login(request, user)
                #uu = request.session['signupp_id']
                #return HttpResponse(uu)
                #request.session['email_confirmed'] = True 
                
            # else:
            #     context['error'] = "Error in Connection"
            #     return render(request, 'S_W/error.html', context)
        else:
            #context[error] = "ERROR"
            #return HttpResponse("eeeoooorrrrooror")
            return render(request, 'login/login.html')
    # except:
        
    #     return render(request, 'login/login.html')


def home(request):
    request.session.set_expiry(300)
    try:
        new_id = request.session['user_id']
        if new_id:
            return render(request, 'login/index.html')
    except:
        return render(request, 'login/login.html')

def logout(request):
   try:
      print('heyy')
      del request.session['user_id']
      del request.session['email']
   except:
      pass
   return HttpResponseRedirect(reverse('home'))

