from django.shortcuts import render
from .models import admin,hr,manager,employ,send_report,get_report,request_leave,approve_leave
from django.db.models import Q
# Create your views here.

def admin_reg(request):   # registeration for admin
    if request.method =='POST':
        name = request.POST.get('name')
        ad_code = request.POST.get('ad_code')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phnum = request.POST.get('phnum')
        date= request.POST.get('date')
        password = request.POST.get('password')

        password1 = request.POST.get('password1')
        if admin.objects.filter(admin_code=ad_code).exists():
            return render(request,'admin_reg.html',{'mgs1':'ADMIN CODE IS ALREADY TAKEN'})
        elif password == password1:
            create1= admin.objects.create(username = name,admin_code = ad_code,phnum = phnum,address = address,password=password,join_date = date,email = email)
            create1.save()
        else:
            return render(request,'admin_reg.html',{'mgs':'PASSWORD IS INCORRECT'})
    return render(request,'admin_reg.html')

def emp_reg(request):   # registeration for employee
    if request.method =='POST':
        name = request.POST.get('name')
        ad_code = request.POST.get('emp_code')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phnum = request.POST.get('phnum')
        date= request.POST.get('date')
        skill= request.POST.get('skill')
        score = request.POST.get('score')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if employ.objects.filter(admin_code=ad_code).exists():
            return render(request,'employ_reg_reg.html',{'mgs1':'ADMIN CODE IS ALREADY TAKEN'})
        elif password == password1:
            create1= employ.objects.create(username = name,skill = skill,score=score,admin_code = ad_code,phnum = phnum,address = address,password=password,join_date = date,email = email)
            create1.save()
        else:
            return render(request,'employ_reg.html',{'mgs':'PASSWORD IS INCORRECT'})
    return render(request,'employ_reg.html')
        
def hr_reg(request):  # registeration for hr
    if request.method =='POST':
        name = request.POST.get('name')
        hr_code = request.POST.get('hr_code')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phnum = request.POST.get('phnum')
        date= request.POST.get('date')
        password = request.POST.get('password')

        password1 = request.POST.get('password1')
        if hr.objects.filter(hr_code=hr_code).exists():
            return render(request,'hr_reg.html',{'mgs1':'ADMIN CODE IS ALREADY TAKEN'})
        elif password == password1:
            create1= hr.objects.create(username = name,hr_code = hr_code,phnum = phnum,address = address,password=password,join_date = date,email = email)
            create1.save()
        else:
            return render(request,'hr_reg.html',{'mgs':'PASSWORD IS INCORRECT'})
    return render(request,'hr_reg.html')

def manager_reg(request):  # registeration for manager
    if request.method =='POST':
        name = request.POST.get('name')
        manager_code = request.POST.get('manager_code')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phnum = request.POST.get('phnum')
        date= request.POST.get('date')
        password = request.POST.get('password')

        password1 = request.POST.get('password1')
        if manager.objects.filter(manager_code=manager_code).exists():
            return render(request,'manager_reg.html',{'mgs1':'ADMIN CODE IS ALREADY TAKEN'})
        elif password == password1:
            create1= manager.objects.create(username = name,manage_code = manager_code,phnum = phnum,address = address,password=password,join_date = date,email = email)
            create1.save()
        else:
            return render(request,'manager_reg.html',{'mgs':'PASSWORD IS INCORRECT'})
    return render(request,'manager_reg.html')

def login(request): # login function

    if request.method == 'POST':
        
        name = request.POST.get('name')       
        ad_code = request.POST.get('ad_code')
        password = request.POST.get('password')
        
        print(name,ad_code,password)
        
        admin1 = admin.objects.filter(admin_code=ad_code) 
        admin2 = employ.objects.filter(admin_code=ad_code)
        admin3 = hr.objects.filter(hr_code=ad_code)
        admin4 = manager.objects.filter(manager_code =ad_code)

        print(admin1,admin2,admin3,admin4)
        
        if str(admin1) != '<QuerySet[]>': #login for admin
            for i in admin1:
                print("admin")
                ad_code = i.admin_code
                name = i.username
                request.session['admincode'] = ad_code
                request.session['user'] = name
                return render(request,'Admin_main.html',{'bankmain':name})
            
        if str(admin2) != '<QuerySet[]>':  #login for employee
            for i in admin2:
                print("employee")
                emp_code = i.admin_code
                name = i.username
                request.session['employcode'] = emp_code
                request.session['user'] = name
                return render( request,'employ_main.html',{'employname':name})
            
            
        if str(admin3) != '<QuerySet[]>':  #login for hr
            for i in admin3:
                print('hr')
                hr_code = i.hr_code
                name = i.username
                request.session['hrcode'] = hr_code
                request.session['user'] = name
                return render(request,'hr_main.html',{'hrname':name})
            
        if str(admin4) != '<QuerySet[]':  #login for manager
            for i in admin4:
                print("manager")
                manager_code = i.manager_code
                name = i.username
                request.session['manager_code'] = manager_code
                request.session['user'] = name
                return render(request,'manager_main.html',{'managername': name})         
        
        else:
            return render(request,'login.html',{'mgs':'INVALID LOGIN'})
    return render(request,'login.html') 

def edit_emp(request):    # to edit the employee data by the admin
    
    name = employ.objects.all()
    if request.method == 'POST':
    
        na = request.POST.get('name')
        code = request.POST.get('emp_code')
        address = request.POST.get('address')
        joindate = request.POST.get('join_date')
        skill = request.POST.get('skill')
        score = request.POST.get('score')
        email = request.POST.get('email')
        phnum =request. POST. get('phnum')
        password =request.POST.get('password')
        print(na,code,address)

        try:
            edits = employ.objects.filter(admin_code = code)
            print(edits)
            for edit in edits:
                edit.username = na
                edit.address = address
                edit.skill = skill
                edit.email = email
                edit.phnum = phnum
                edit.password = password
                edit.save()
                print("data saved")
                return render(request,'login.html',{'mgs':'DATA SAVED SUCCESSFULLY'})
            
                
        except Exception as a:
            print(a)
            print("data not saved")
            return render(request,'edit_employ.html',{'mgs':'UNABLE TO EDIT'})
        
    return render(request,'edit_employ.html',{'data':name})

            
def edit_admin(request): # edit admin details by admin
    if request.method == 'POST':
        
        na = request.POST.get('name')
        code = request.POST.get('ad_code')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phnum =request. POST. get('phnum')
        password = request.POST.get('password')
        
        try:
            edit1 = admin.objects.filter(admin_code= code)
            for edit in edit1:
                edit.username = na
                
                edit.address = address
                edit.email = email
                edit.phnum = phnum
                if edit.password == password:
                    edit.save()
                    print("data saved")
                    return render(request,'login.html',{'mgs':'DATA EDITED SUCCESSFULLY'})
                else:
                    return render(request,'admin_edit.html',{'mgs':'UNABLE TO EDIT DATA'})
                    
        except Exception as a:
            print(a)
            return render(request,'admin_edit.html',{'mgs':'UNABLE TO EDIT DATA'})
  
    return render(request,'admin_edit.html')


def edit_hr(request):   #edit hr details by admin
    all = hr.objects.all()
    if request.method == 'POST':
        
        na = request.POST.get('name')
        code = request.POST.get('hr_code')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phnum =request. POST. get('phnum')
        password = request.POST.get('password')
        print(na,code,address)
        try:
            edit1 = hr.objects.filter(hr_code= code)
            for edit in edit1:
                edit.username = na
                edit.address = address
                edit.email = email
                edit.phnum = phnum
                edit.save()
                print("data saved")
                return render(request,'login.html',{'mgs1':'DATA EDITED SUCCESSFULLY'})
            
        except Exception as a:
            print(a)
            return render(request,'hr_edit.html',{'mgs':'UNABLE TO EDIT DATA'})
  
    return render(request,'hr_edit.html',{'data':all})

def edit_managerbyad(request): # edit manager data by admin
        a = manager.objects.all()
        if request.method == 'POST':
        
            na = request.POST.get('name')
            code = request.POST.get('manager_code')
            address = request.POST.get('address')
            email = request.POST.get('email')
            phnum =request. POST. get('phnum')
            password = request.POST.get('password')
            
            try:
                edit1 = manager.objects.filter(manager_code= code)
                for edit in edit1:
                    edit.username = na
                    edit.address = address
                    edit.email = email
                    edit.phnum = phnum
                    if edit.password == password:
                        edit.save()
                        print("data saved")
                        return render(request,'login.html',{'mgs1':'DATA EDITED SUCCESSFULLY'})
                    else:
                        return render(request,'manager_editbyadmin.html',{'mgs':'UNABLE TO EDIT DATA'})
                        
            except Exception as a:
                print(a)
                return render(request,'manager_editbyadmin.html',{'mgs':'UNABLE TO EDIT DATA'})
            
        return render(request,'manager_editbyadmin.html',{'data1':a})
    

def edit_manager(request):   # edit manager details by manager
    print("running")
    a = request.session['manager_code']
    b = manager.objects.get(manager_code = a)
    print(b)
    if request.method == 'POST':
        
        na = request.POST.get('name')
        code = request.POST.get('manager_code')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phnum =request. POST. get('phnum')
        password = request.POST.get('password')
            
        try:
            edit1 = manager.objects.filter(manager_code= code)
            for edit in edit1:
                edit.username = na
                edit.address = address
                edit.email = email
                edit.phnum = phnum
                if edit.password == password:
                    edit.save()
                    print("data saved")
                    return render(request,'manager_main.html',{'mgs1':'DATA EDITED SUCCESSFULLY'})
                else:
                    return render(request,'manager_edit.html',{'mgs':'UNABLE TO EDIT DATA'})
                        
        except Exception as a:
            print(a)
            return render(request,'manager_edit.html',{'mgs':'UNABLE TO EDIT DATA'})
            
    return render(request,'manager_edit.html',{'data':b})
    
def edit_employee(request): # edit employee details by employee
    a = request.session['employcode']
    b = employ.objects.get(admin_code = a)
    if request.method == 'POST':
        
        na = request.POST.get('name')
        code = request.POST.get('emp_code')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phnum =request. POST. get('phnum')
        skill = request.POST. get('skill')
        score = request.POST.get('score')
        password = request.POST.get('password')
        
        try:
            edit1 = employ.objects.filter(admin_code= code)
            for edit in edit1:
                edit.username = na
                edit.score = score
                edit.skill = skill
                edit.address = address
                edit.email = email
                edit.phnum = phnum
                if edit.password == password:
                    edit.save()
                    print("data saved")
                    return render(request,'employee_edit.html',{'mgs':'DATA EDITED SUCCESSFULLY'})
                else:
                    return render(request,'employee_edit.html',{'mgs':'UNABLE TO EDIT DATA'})
                    
        except Exception as a:
            print(a)
            return render(request,'employee_edit.html',{'mgs':'UNABLE TO EDIT DATA'})
  
    return render(request,'employee_edit.html',{'data':b})

def search_emp(request):   #searching the employeee  
    code = employ.objects.all()
    if request.method == 'POST':
        search = request.POST.get('code')
        code= employ.objects.filter(admin_code =search)
        
    return render(request,'search_employee.html',{'data':code})

def searchemp_hr(request): # search employee by hr
    if 'submit' in request.POST:
        s = request.POST.get('code')
        code1 = employ.objects.filter(Q(admin_code__contains = s))
        return render(request,'searchemp_byhr.html',{'data':code1})
    else:
        code2 = employ.objects.all()
        return render(request,'searchemp_byhr.html',{'data':code2})



def searchemp_mana(request): # search employee by mamager
    
    if 'submit' in request.POST:
        s = request.POST.get('code')
        code1 = employ.objects.filter(Q(admin_code__contains = s))
        return render(request,'searchemp_bymana.html',{'data':code1})
    else:
        code2 = employ.objects.all()
        return render(request,'searchemp_bymana.html',{'data':code2})

     
def send_report1(request): #send report by employee
    try:
        if request.method =="POST":
            name = request.POST.get('name')
            emp_code = request.POST.get('emp_code')
            pro_name = request.POST.get('pro_name')
            pro_progress = request.POST.get('pro_progress')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            send1 = send_report.objects.create(username=name,usercode=emp_code,project_name=pro_name,project_progress=pro_progress,project_date = start_date,end_date=end_date)
            send1.save()
        return render(request,'send_report.html',{'mgs':'REPORT SENDED SUCCESSFULLY!!!'})
    except Exception as a:
        return render(request,'send_report.html',{'mgs': 'CAN NOT ABLE TO SENT THE REPORT!!!'})  
    
def request_leave1(request): #requested by employee
    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('emp_code')
        c = request.POST.get('reason')
        d = request.POST.get('day')
        ag = request_leave.objects.create(emp_name = a,emp_code = b,reason = c,days = d)
        ag.save()
        return render(request,'request_leave.html',{'mgs':'REQUEST SENT SUCCESSFULLY'})
    return render(request,'request_leave.html')

def approve_leave1(request): # request approved by hr
    a1 = request_leave.objects.all()
    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('emp_code')
        c = request.POST.get('reason')
        d = request.POST.get('day')
        ag1 = request_leave.objects.filter(emp_code = b)
        ag1.delete()
        ag = approve_leave.objects.create(emp_name = a,emp_code = b,reason = c,days = d)
        ag.save()
        return render(request,'hr_main.html')
    return render(request,'approveleave.html',{'data':a1})
        

def all_members(request):
    b = employ.objects.all()
    c = hr.objects.all()
    d = manager.objects.all()
    return render(request,'allmembers.html',{'data1':b,'data2':c,'data3':d})
 
def get_report1(request): #getting report by hr
    code = send_report.objects.all()
    return render(request,'get_reportbyhr.html',{'data':code})

def get_report2(request): #getting report by manager
    code = send_report.objects.all()
    return render(request,'get_reportbymana.html',{'data':code})

def all_admin(request): # to see all admin
    user = admin.objects.all()
    return render(request,'our_admin.html',{'mgs':user})        

def ad_main(request): # main page of admin
    bankmain = request.session['user']
    return render(request,'Admin_main.html',{'bankmain':bankmain})  

def emp_main(request): # main page for employee
    bankmain = request.session['user']
    return render(request,'employ_main.html',{'employname':bankmain,})  

def hr_main(request):  # main page for hr
    bankmain = request.session['user']
    return render(request,'hr_main.html',{'hrname':bankmain})  

def manager_main(request):  # main page for manager
    return render(request,'manager_main.html')  
