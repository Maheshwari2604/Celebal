# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.




class Employee(models.Model):
    #code = models.CharField(db_column='Code', primary_key=True, max_length=3)  # Field name made lowercase.
    name = models.CharField(max_length=100)  # Field name made lowercase.
    title = models.CharField(null=True ,max_length=100)  # Field name made lowercase.
    team = models.CharField(null=True ,max_length=100)  # Field name made lowercase.
    manager = models.CharField(null=True ,max_length=100)  # Field name made lowercase.
    manager_emp_id = models.CharField(null=True ,max_length=100)  # Field name made lowercase.
    asset_type = models.CharField(null=True ,max_length=100)  # Field name made lowercase.
    
    def __str__(self):
        return str(self.id)


class Project(models.Model):
    projectname = models.CharField(max_length=100)  # Field name made lowercase.
    manager_emp_id = models.CharField(max_length=100)  # Field name made lowercase.
    startdate = models.DateField()  # Field name made lowercase.
    enddate = models.DateField()  # Field name made lowercase.
    billed_assets = models.IntegerField(null=True)  # Field name made lowercase.
    budget = models.CharField(null=True , max_length=50)  # Field name made lowercase.
    partner = models.CharField(null=True , max_length=200)  # Field name made lowercase.
    sales_person_id = models.CharField(null=True , max_length=1000)  # Field name made lowercase.
    paid = models.CharField(null=True , max_length=10)  # Field name made lowercase.

    def __str__(self):
        return str(self.id)


class task(models.Model):
    type = models.CharField(max_length = 15)

    def __str__(self):
        return str(self.type)

class task(models.Model):
    type = models.CharField(max_length = 15)

    def __str__(self):
        return (self.id)


class timesheet(models.Model):
    #project = models.ForeignKey(Project , on_delete=models.CASCADE)  # Field name made lowercase.
    #emp_id = models.ForeignKey(Employee , on_delete=models.CASCADE)
    #task_type = models.ForeignKey(task, on_delete=models.CASCADE)
    projectid = models.IntegerField()
    emp_id = models.CharField(null=True , max_length=510)   # Field name made lowercase.
    bill_date = models.DateTimeField(auto_now=False, auto_now_add=True)  # Field name made lowercase.
    task_type = models.ForeignKey(task, on_delete=models.CASCADE)  # Field name made lowercase.
    billed_hours = models.CharField(null=True , max_length=510)  # Field name made lowercase.
    task_description = models.CharField(null=True , max_length=510)  # Field name made lowercase.
    isapproved = models.CharField(null=True , max_length=510)
    approved_by_emp_id = models.CharField(null=True , max_length=510)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)  # Field name made lowercase.

    def __str__(self):
        return str(self.id)

