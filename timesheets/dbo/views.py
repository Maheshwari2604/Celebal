# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render , HttpResponse
from .models import Employee , Project , timesheet
# Create your views here.
def employee(request):
        #try:
                if request.method == 'POST':
                        print('in post')
                        name = request.POST['name']
                        title = request.POST['title']
                        team = request.POST['team']
                        manager_name = request.POST['manager_name']
                        manager_email = request.POST['manager_email']
                        asset_type = request.POST['asset_type']
                        user = Employee()
                        user.name = name
                        user.title = title
                        user.team = team
                        user.manager_name = manager_name
                        user.manager_email = manager_email
                        user.asset_type = asset_type
                        print(user.name)
                        #print(user.AClass)
                        #print(completed)    
                        user.save()
                        return render(request , 'dbo/employeedetail.html')
                else:
                        print('in else')
                        return render(request , 'dbo/employeedetail.html')
        # except:
        #         print('in except')
        #         return render(request , 'dbo/employeedetail.html')

def project(request):
        try:
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
                        return render(request , 'dbo/projectdetail.html')
                else:
                        print('in else')
                        return render(request , 'dbo/projectdetail.html')
        except:
                print('in except')
                return render(request , 'dbo/projectdetail.html')

def view_projects(request):

        return render(request , 'dbo/viewproject.html')
        
def timesheets(request):
        try:
                if request.method == 'GET':
                        print('in get')
                        user = timesheet()
                        project = request.GET['project_id']
                        
                        #print(project)
                        project = Project.objects.get(projectname=project)
                        project = project.id
                        print(project)
                        user.project = project
                        print(user.project)
                        user.emp_id = request.GET['emp_id']
                        print(user.emp_id)
                        user.task_type = request.GET['tasktype']
                        print(user.task_type)
                        user.task_description = request.GET['task_description']
                        user.billed_hours = request.GET['billed_hours']
                        print(user.task_description)
                        #print(user)
                        user.approved_by_emp_id = request.GET['approved_by_emp_id']
                        print(user.approved_by_emp_id)
                        user.isapproved = 'N'
                        # print(user.isapproved)
                        user.save()
                        #project = Project.objects.all()
                        context = {
                                'message': 'Thanks for submission'
                                
                        }
                        return render(request , 'dbo/timesheets.html' , context)
                else:
                        print('in else')
                        project = Project.objects.all()

                        #taking project model and message                                       
                        context = {
                                "message": 'Please fill the form',
                                "project": project
                        }
                        return render(request , 'dbo/timesheets.html' , context)
        except:
                project = Project.objects.all()

                context={
                                "message": 'Please fill the form',
                                "project": project
                        }
                return render(request , 'dbo/timesheets.html' , context)