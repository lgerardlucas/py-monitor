from rest_framework.viewsets import ModelViewSet
from app_monitor.models import Monitor
from .serializers import MonitorSerializer

class MonitorViewSet(ModelViewSet):
    queryset = Monitor.objects.all().order_by('-id','date_insert','company_document','key_name','identify_name')
    serializer_class = MonitorSerializer

