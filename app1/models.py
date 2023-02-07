from django.db import models
from django.utils import timezone

# Create your models here.

class admin(models.Model):
    username = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    admin_code = models.CharField(max_length=10,blank=True,null=True)
    join_date = models.DateField(blank=True,null=True)
    email =models.EmailField(default="unknown@gmail.com")
    password = models.CharField(max_length=10,blank=True,null=True)
    phnum = models.IntegerField(blank=True,null=True)
    

    
class employ(models.Model):
    username = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    score = models.IntegerField(blank=True,null=True)
    admin_code = models.CharField(max_length=10,blank=True,null=True)
    join_date = models.DateField(blank=True,null=True)
    email =models.EmailField(default="unknown@gmail.com")
    password = models.CharField(max_length = 10,blank=True,null=True)
    phnum = models.IntegerField(blank=True,null=True)
    skill = models.CharField(max_length=100,blank=True,null=True)
    roll = models.CharField(max_length=100,blank=True,null=True)

    
class hr(models.Model):
    username = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    hr_code = models.CharField(max_length=10,blank=True,null=True)
    join_date = models.DateField(blank=True,null=True)
    email =models.EmailField(default="unknown@gmail.com")
    password = models.CharField(max_length=10,blank=True,null=True)
    phnum = models.IntegerField(blank=True,null=True)
    roll = models.CharField(max_length=100,blank=True,null=True)

    
class manager(models.Model):
    username = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    manager_code = models.CharField(max_length=10,blank=True,null=True)
    join_date = models.DateField(blank=True,null=True)
    email =models.EmailField(default="unknown@gmail.com")
    password = models.CharField(max_length=10,blank=True,null=True)
    phnum = models.IntegerField(blank=True,null=True)
    roll = models.CharField(max_length=100,blank=True,null=True)

class send_report(models.Model):
    username = models.CharField(max_length=100,blank=True,null=True)
    usercode = models.CharField(max_length=10,blank=True,null=True)
    project_name = models.CharField(max_length=100,blank=True,null=True)
    project_progress = models.CharField(max_length=100,blank=True,null=True)
    project_date = models.DateField(timezone.now(),blank=True,null=True)
    end_date = models.DateField(timezone.now(),blank=True,null=True)

class get_report(models.Model):
    username = models.CharField(max_length=100,blank=True,null=True)
    usercode = models.CharField(max_length=10,blank=True,null=True)
    project_name = models.CharField(max_length=100,blank=True,null=True)
    project_progress = models.CharField(max_length=100,blank=True,null=True)
    project_date = models.DateField(timezone.now(),blank=True,null=True)
    end_date = models.DateField(timezone.now(),blank=True,null=True)
    
class request_leave(models.Model):
    emp_name = models.CharField(max_length=100,blank=True,null=True)
    emp_code = models.CharField(max_length=10,blank=True,null=True)
    reason = models.CharField(max_length=100,blank=True,null=True)
    days = models.IntegerField(blank=True,null=True)
    
class approve_leave(models.Model):
    emp_name = models.CharField(max_length=100,blank=True,null=True)
    emp_code = models.CharField(max_length=10,blank=True,null=True)
    reason = models.CharField(max_length=100,blank=True,null=True)
    days = models.IntegerField(blank=True,null=True)