from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Baza_client, TypeCase, StatusCase

class OrderSeriaLizer(ModelSerializer):
    # type_case = PrimaryKeyRelatedField(source='type_case.NameTypeCase' ,queryset=TypeCase.objects.all(), many=False)
    # status_case = PrimaryKeyRelatedField(source='status_case.NameStatusCase' ,queryset=StatusCase.objects.all(), many=False)
    
    type_case = serializers.SlugRelatedField( many=False, queryset=TypeCase.objects.all(), slug_field='NameTypeCase')
    status_case = serializers.SlugRelatedField( many=False,queryset=StatusCase.objects.all(), slug_field='NameStatusCase')
    class Meta:
        model = Baza_client
        
        fields = ["id",'name_client', 'contract_number', 'date_contract', 'type_case', 'date', 'status_case', 'documents_case']

       