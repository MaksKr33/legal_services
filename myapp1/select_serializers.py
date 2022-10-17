from rest_framework.serializers import ModelSerializer
from .models import TypeCase

class TypeCaseSeriaLizer(ModelSerializer):
    
    class Meta:
        model = TypeCase
        fields = ['id','NameTypeCase']