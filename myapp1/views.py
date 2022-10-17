# from warnings import filters
from django.shortcuts import render, redirect
from .models import Baza_client, StatusCase , TypeCase
from .forms import Baza_client_Form
from rest_framework.viewsets import ModelViewSet
from .serializers import OrderSeriaLizer
from .type_case_serializers import TypeCaseSeriaLizer
from . status_case_serializers import StatusCaseSeriaLizer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# from django.views.generic.base import View

def base(request):
    return render(request,'myapp1/base.html')

def new_client(request):
    error = ''
    if request.method == 'POST':
        form = Baza_client_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = f"{form.errors} \n {form.data}"

    form = Baza_client_Form()
    context = {
        'form': form,
       'error': error}
    return render(request,'myapp1/new_client.html', context)

# def contact(request):
#     clients = Baza_client.objects.all()
#     return render(request,'myapp1/contact_page.html', {'name_clients': 'База клієнтів', 'Klient': clients })

def contact_new(request):
    return render(request,'myapp1/contact_page.html')


class OrederViews(ModelViewSet):
    queryset = Baza_client.objects.all()
    serializer_class = OrderSeriaLizer
    filter_backends= [DjangoFilterBackend, OrderingFilter , SearchFilter]
    filterset_fields = ['type_case']
    ordering_fields = ['name_client', 'contract_number']
    search_fields = ['name_client', 'contract_number'] 

class TypeViews(ModelViewSet):
    queryset = TypeCase.objects.all()
    serializer_class = TypeCaseSeriaLizer


class StatusViews (ModelViewSet):
    queryset = StatusCase.objects.all()
    serializer_class =  StatusCaseSeriaLizer
    
    
   
 