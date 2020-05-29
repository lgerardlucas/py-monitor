from django.contrib import admin
from .models import Monitor

class MonitorAdmin(admin.ModelAdmin):
	list_display = ('id','company_document','company_name','key_name','identify_name','data_value','date_insert','system_version')

admin.site.register(Monitor,MonitorAdmin)
