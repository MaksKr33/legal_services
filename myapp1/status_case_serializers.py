from rest_framework.serializers import ModelSerializer
from .models import StatusCase

class StatusCaseSeriaLizer(ModelSerializer):
    
    class Meta:
        model = StatusCase
        fields = ['id','NameStatusCase']