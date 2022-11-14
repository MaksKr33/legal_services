from django.views.generic import UpdateView, DeleteView
from django.shortcuts import render, redirect
from myapp1.models import StatusCase, TypeCase , Baza_client
from .models import Baza_client, StatusCase, TypeCase 
from .forms import Baza_client_Form
from rest_framework.viewsets import ModelViewSet
from .serializers import OrderSeriaLizer, StatusCaseSeriaLizer, TypeCaseSeriaLizer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.urls import reverse_lazy
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


def base(request):
    return render(request,'myapp1/base.html')

def informations(request):
    return render(request,'myapp1/informations.html')
    

def new_client(request):
    error = ''
    if request.method == 'POST':
        form = Baza_client_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = "Введіть правильні дані"

    form = Baza_client_Form()
    context = {
        'error': error,
         'form': form}
    return render(request,'myapp1/new_client.html', context)


class UpdateClients(UpdateView):
    model= Baza_client
    template_name = 'myapp1/new_client.html'
    form_class = Baza_client_Form

    
def contact_new(request):
    return render(request,'myapp1/contact_page.html')


class OrederViews(ModelViewSet):
   
    queryset = Baza_client.objects.all()
    serializer_class = OrderSeriaLizer
    # permission_classes = [IsAuthenticated]
    filter_backends= [DjangoFilterBackend, OrderingFilter , SearchFilter]
    filterset_fields = ['type_case', 'date', 'status_case', 'date_contract']
    ordering_fields = ['name_client', 'contract_number']
    search_fields = ['name_client', 'contract_number'] 

    def destroy (self, request, *args, **kwargs):
        client_del = self.get_object()
        client_del.delete()
        return Response({'messsage' : "Delete user"})

class TypeViews(ModelViewSet):
    queryset = TypeCase.objects.all()
    serializer_class =  TypeCaseSeriaLizer

class StatusViews (ModelViewSet):
    queryset = StatusCase.objects.all()
    serializer_class =  StatusCaseSeriaLizer
    


   
   
 