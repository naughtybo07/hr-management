from django.urls import path
from app1 import views

urlpatterns = [
    path('login',views.login,name="login"), 
    
    path('admin_main',views.ad_main,name="admin main"),
    path('admin_reg',views.admin_reg,name="admin register"),
    path('empy_reg',views.emp_reg,name="employ register by admin"),
    path('manager_reg',views.manager_reg,name="manager register by admin"),
    path('hr_reg',views.hr_reg,name="hr register by admin"),
    path('editadmin',views.edit_admin,name = 'edit admin details'),
    path('alladmin',views.all_admin,name="all admin details"),
    path('edithr',views.edit_hr,name="edit hr detail by admin"),
    path('editmana',views.edit_managerbyad,name="edit manager by admin"),
    path('editemploye',views.edit_emp,name="edit employee BY admin"), 
    path('alluser',views.all_members,name = "view all members"),
   
    
    path('edit_employ',views.edit_employee,name="edit employee detail by employee"), 
    path('employ_main',views.emp_main,name="employ main"),    
    path('sendreport',views.send_report1,name="send report by employ"),
    path('requestleave',views.request_leave1,name="request for leave"),
    path('searchemploy',views.search_emp,name="search employee"),

    path('getreportbyhr',views.get_report1,name="get report by hr"),
    path('searchempbyhr',views.searchemp_hr,name="search emp by hr"),
    path('hr_main',views.hr_main,name="hr main"),
    path('approveleave',views.approve_leave1,name='approve leave by hr'),

    path('getreportbymana',views.get_report2,name="get report by manager"),
    path('manager_main',views.manager_main,name="manager main"),
    path('editmanager',views.edit_manager,name="edit manager detail by manager"),
   
    path('searchempbymana',views.searchemp_mana,name="search employee by manager"),
    
    
]
