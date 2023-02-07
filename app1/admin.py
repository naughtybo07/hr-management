from django.contrib import admin
from app1 import models

# Register your models here.

admin.site.register([models.admin,models.employ,models.hr,models.manager,models.get_report,models.send_report,models.request_leave,models.approve_leave])