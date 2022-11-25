from .models import Baza_client
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput,  NumberInput, DateInput, Select, ClearableFileInput,FileInput
 

class Baza_client_Form (forms.ModelForm):
      
       def __init__(self, *args, **kwargs):
              super().__init__(*args, **kwargs)
              self.fields['type_case'].empty_label = "Тип справи"
              self.fields['status_case'].empty_label = "Статус справи"
       class Meta: 
              model = Baza_client  
             
              fields = ['name_client', 'contract_number', 'date_contract', 'type_case', 'date', 'status_case', 'documents_case']
              widgets = {'name_client': TextInput(attrs={
                     'class': 'form-control',
                     'placeholder': 'Введіть ПІБ'  }),

                     'contract_number': NumberInput(attrs={
                     'class': 'form-control',
                     'placeholder': 'Введіть номер договору'  }),

                     'date_contract': DateInput(attrs={
                     'class': 'form-control',
                     'placeholder': 'Дата договору'  }),

                     'type_case': Select(attrs={
                     'class': 'form-select',
                     'value':   'Тип справи'}),

                     'date':  DateInput(attrs={
                     'class': 'form-control',
                     'placeholder' : 'Дата подачі справи'  }),

                     'status_case' :  Select(attrs={
                    'class': 'form-select',
                     'value':   'Тип справи'
                     } ),

                     'documents_case' :FileInput(attrs={
                     'class': 'btn btn-outline-primary ',
                     'placeholder': 'Загрузка документів'  } ) }



class RegisterUserForm(UserCreationForm):

       username = forms.CharField(label= 'Логін', widget= forms.TextInput (attrs= {'class':  'form-control' }))
       password1 = forms.CharField(label= 'Пароль', widget= forms.PasswordInput (attrs= {'class': 'form-control' }))
       password2 = forms.CharField(label= 'Повторний пароль', widget= forms.PasswordInput (attrs= {'class':'form-control' }))
       
       model = User
       fields = ['username' , 'password1', 'password2']
       widgets = {
              'username' : forms.TextInput (attrs= {'class':  'form-control' }),
              'password1' : forms.PasswordInput (attrs= {'class': 'form-control' }),
              'password2' : forms.PasswordInput (attrs= {'class': 'form-control' })
       }


class LoginUserForm(AuthenticationForm):

       username = forms.CharField(label= 'Логін', widget= forms.TextInput (attrs= {'class':  'form-control' }))
       password = forms.CharField(label= 'Пароль', widget= forms.PasswordInput (attrs= {'class': 'form-control' }))