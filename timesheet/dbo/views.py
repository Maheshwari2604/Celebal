# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render , HttpResponse
from .models import Employee , Project , timesheet , task , asset_type
# Create your views here.


def employee(request):
                request.session.set_expiry(300)
        #try:
                new_id = request.session['user_id']
                if new_id: 
                        #print(new_id)
                        #try:
                                if request.method == 'POST':
                                        print('in post')
                                        print(new_id)
                                        name = request.POST['name']
                                        title = request.POST['title']
                                        team = request.POST['team']
                                        manager_name = request.POST['manager_name']
                                        manager_email = request.POST['manager_email']
                                        asset_typee = request.POST['asset_type']
                                        user = Employee()
                                        user.name = name
                                        user.title = title
                                        user.team = team
                                        user.manager_name = manager_name
                                        user.manager_email = manager_email
                                        user.asset_type = asset_typee
                                        print(user.name)
                                        #print(user.AClass)
                                        #print(completed)    
                                        user.save()
                                        asset_types = asset_type.objects.all()
                                        context ={
                                                "asset_type": asset_types
                                        }
                                        return render(request , 'dbo/employeedetail.html' , context)
                                else:
                                        print('in else')
                                        asset_types = asset_type.objects.all()
                                        context = {
                                                "asset_types": asset_types
                                        }
                                        return render(request , 'dbo/employeedetail.html', context)
                
                        # except:
                        #         asset_type = asset_type.objects.all()
                        #         context ={
                        #                 "asset_types": asset_type
                        #         }
                        #         return render(request , 'dbo/employeedetail.html', context)
        # except:
        #         print('in except')
        #         return render(request , 'login/login.html')

def project(request):
                request.session.set_expiry(300)
        #try:
                print('in try')
                new_id = request.session['user_id']
                if new_id:
                        try:
                                print(new_id)
                                if request.method == 'GET':
                                        print('in post')
                                        user = Project()
                                        #user.project = request.GET['projectname']
                                        user.projectname = request.GET['projectname']
                                        user.manager_emp_id = request.GET['manager_emp_id']
                                        user.team = request.GET['team']
                                        user.startdate = request.GET['startdate']
                                        user.enddate = request.GET['enddate']
                                        user.asset_type = request.GET['billed_assets']
                                        user.partner = request.GET['partner']
                                        user.budget = request.GET['budget']
                                        user.sales_person_id = request.GET['sales_person_id']
                                        user.paid = request.GET['paid']
                                        print(user.paid)
                                        user.save()
                                        context = {
                                                'message': 'Thanks for Submission'
                                        }
                                        return render(request , 'dbo/projectdetail.html', context)
                                else:
                                        context = {
                                                'message': 'Enter New Project'
                                        }
                                        print('in else')
                                        return render(request , 'dbo/projectdetail.html', context)
                        except:
                                context = {
                                        'message': 'Enter New Project'
                                }
                                print('in else2')
                                return render(request , 'dbo/projectdetail.html', context)
        # except:
        #         print('in except')
        #         return render(request , 'login/login.html')

def view_projects(request):
        request.session.set_expiry(300)
        try:
                print('in try')
                new_id = request.session['user_id']
                email = request.session['email']
                if new_id:
                        print(new_id)
                        timesheets = timesheet.objects.filter(emp_id=email)
                        context = {
                            "timesheet": timesheets
                        }
                        return render(request , 'dbo/viewproject.html' , context)
        except:
                return render(request , 'login/login.html')        
        


def timesheets(request):
                request.session.set_expiry(300)
        #try:
                print('in try')
                new_id = request.session['user_id']
                if new_id:
                        #print(new_id)
                                email = request.session['email']
                        #print(email)
                        #try:
                                if request.method == 'GET':
                                        print('in get')
                                        user = timesheet()
                                        project = request.GET['project_id']
                                        tasks = task()                        
                                        #print(project)
                                        project = Project.objects.get(projectname=project)
                                        project = project.id
                                        
                                        user.projectid = project
                                        
                                        user.emp_id = email
                                        
                                        tasks.type = request.GET['tasktype']
                                        
                                        type = tasks.type
                                        
                                        user.task_type = type
                                        
                                        user.task_description = request.GET['task_description']
                                        user.billed_hours = request.GET['billed_hours']
                                        user.bill_date = request.GET['billdate']
                                        user.approved_by_emp_id = request.GET['approved_by_emp_id']
                                        user.isapproved = 'N'
                                        # print(user.isapproved)
                                        user.save()
                                        
                                        #project = Project.objects.all()
                                        project = Project.objects.all()
                                        tasks = task.objects.all()
                                        Employe = Employee.objects.all()
                                        print(Employe)
                                        context = {
                                                "message": 'Thanks for submission',
                                                "tasks": tasks,
                                                "project": project,
                                                "Employee": Employe
                                        }
                                        return render(request , 'dbo/timesheets.html' , context)
                                else:
                                        print('in else')
                                        project = Project.objects.all()
                                        tasks = task.objects.all()
                                        Employe = Employee.objects.all()
                                        context = {
                                                "message": 'Please fill the form',
                                                "tasks": tasks,
                                                "project": project,
                                                "Employee": Employe
                                        }
                                        return render(request , 'dbo/timesheets.html' , context)
        
                        # except:
                        #         project = Project.objects.all()
                        #         tasks = task.objects.all()
                        #         Employe = Employee.objects.all()
                        #         context = {
                        #                 "message": 'Please fill the form',
                        #                 "tasks": tasks,
                        #                 "project": project,
                        #                 "Employee": Employe
                        #         }
                        #         return render(request , 'dbo/timesheets.html' , context)
        # except:
        #         print('in exept')
        #         project = Project.objects.all()
        #         tasks = task.objects.all()
        #         context = {
        #                 "message": 'Please fill the form',
        #                 "tasks": tasks,
        #                 "project": project
        #         }
        #         return render(request , 'dbo/timesheets.html' , context)
        # except: 
        #         return render(request , 'login/login.html')


def Aproove_project(request):
        print('hy')
        request.session.set_expiry(300)
        try:
                print('in try')
                print('in try')
                new_id = request.session['user_id']
                email = request.session['email']
                if new_id:
                        print(new_id)
                        timesheets = timesheet.objects.filter(approved_by_emp_id=email)
                        context = {
                            "timesheet": timesheets
                        }
                        return render(request , 'dbo/aproove_project.html' , context)
        except:
                return render(request , 'login/login.html')       


def Aproove_projectt(request, id):
        #print('hy')
        #print(id)
                request.session.set_expiry(300)
        #try:
                print('in try')
                print('in tryw')
                new_id = request.session['user_id']
                email = request.session['email']
                if new_id:
                        if request.method == 'POST':
                                print(new_id)
                                timesheets = timesheet()
                                aproove = request.POST['aprooved']
                                print('aa')
                                print(aproove)
                                if aproove == 'on':
                                        print('true')
                                        timesheets = timesheet.objects.get(id=id)
                                        timesheets.isapproved = 'Y'
                                        
                                else:
                                        print('False')
                                        timesheets = timesheet.objects.get(id=id)
                                        

                                timesheets.save()
                                timesheets = timesheet.objects.filter(approved_by_emp_id=email)
                                context = {
                                "timesheet": timesheets
                                }
                                return render(request , 'dbo/aproove_project.html' , context)
        # except:
        #         return render(request , 'login/login.html')        
