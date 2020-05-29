from rest_framework.serializers import ModelSerializer
from app_monitor.models import Monitor

class MonitorSerializer(ModelSerializer):
    class Meta:
        model = Monitor
        fields = ['id','company_document','company_name','key_name','identify_name','data_value','system_version','date_insert']