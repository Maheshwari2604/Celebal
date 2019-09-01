# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Project , Employee , timesheet , task , asset_type
from django.contrib import admin

# Register your models here.
class project(admin.ModelAdmin):
    list_display = ['id', 'projectname', 'manager_emp_id', 'startdate' ,'enddate', 'billed_assets', 'budget', 'partner' , 'sales_person_id']
    list_editable = ['projectname' , 'manager_emp_id' , 'partner']
    search_fields = ['projectname', 'manager_emp_id' , 'partner']
    date_hierarchy = 'startdate'
    readonly_fields = ['startdate', 'enddate']
    #prepopulated_fields = {"slug": ("username",)}

    class meta:
        model = Project


class employee(admin.ModelAdmin):
    list_display = ['id', 'name', 'title', 'team' ,'manager', 'manager_emp_id', 'asset_type']
    list_editable = ['name' , 'title' , 'team']
    search_fields = ['name', 'title' , 'team']
    #date_hierarchy = 'startdate'
    #readonly_fields = ['startdate', 'enddate']
    #prepopulated_fields = {"slug": ("username",)}

    class meta:
        model = Employee


class timesheets(admin.ModelAdmin):
    list_display = ['id']
    #list_editable = ['name' , 'title' , 'team']
    #search_fields = ['name', 'title' , 'team']
    #date_hierarchy = 'startdate'
    readonly_fields = ['last_updated']
    #prepopulated_fields = {"slug": ("username",)}

    class meta:
        model = timesheet


admin.site.register(Employee , employee)
admin.site.register(Project , project)
admin.site.register(timesheet , timesheets)
admin.site.register(task)
admin.site.register(asset_type)