
from .models import Baza_client
from django import forms
from django.forms.widgets import TextInput,  NumberInput, DateInput, Select, ClearableFileInput,FileInput
 

class Baza_client_Form (forms.ModelForm):
      
       class Meta: 
              model = Baza_client 
              # def __init__(self, *args, **kwargs):
              #        super().__init__(*args, **kwargs)
              #        self.fields['type_case'].empty_label = 'lorem'
                     
              
             
              fields = ['name_client', 'contract_number', 'date_contract', 'type_case', 'date', 'status_case', 'documents_case' ]
              widgets = {'name_client' : TextInput(attrs={
                     'class' : 'form-control',
                     'placeholder' : 'Введіть ПІБ'  }),

                     'contract_number' : NumberInput(attrs={
                     'class' : 'form-control',
                     'placeholder' : 'Введіть номер договору'  }),

                     'date_contract' :DateInput(attrs={
                     'class' : 'form-control',
                     'placeholder' : 'Дата договору'  }),

                     'type_case' : Select(attrs={
                     'class' : 'form-select',
                     'value':   'Тип справи'}

                     ),

                     'date' :  DateInput(attrs={
                     'class' : 'form-control',
                     'placeholder' : 'Дата подачі справи'  }),

                     'status_case' :  Select( attrs={
                    'class' : 'form-select',
                     'value':   'Тип справи'
                     } ),

                     'documents_case' :FileInput(attrs={
                     'class' : 'btn btn-outline-primary ',
                     'placeholder' : 'Загрузка документів'  } )}


