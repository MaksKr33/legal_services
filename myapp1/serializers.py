from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Baza_client, TypeCase, StatusCase

class OrderSeriaLizer(ModelSerializer):
    type_case = PrimaryKeyRelatedField(source='type_case.NameTypeCase' ,queryset=TypeCase.objects.all(), many=False)
    status_case = PrimaryKeyRelatedField(source='status_case.NameStatusCase' ,queryset=StatusCase.objects.all(), many=False)

    class Meta:
        model = Baza_client
        fields = ['name_client', 'contract_number', 'date_contract', 'type_case', 'date', 'status_case', 'documents_case']