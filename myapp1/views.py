from django.views.generic import UpdateView, CreateView
from django.contrib.auth import logout,  authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .models import Baza_client, StatusCase, TypeCase 
from .forms import Baza_client_Form,  LoginUserForm
from rest_framework.viewsets import ModelViewSet
from .serializers import OrderSeriaLizer, StatusCaseSeriaLizer, TypeCaseSeriaLizer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination  

@login_required
def base(request):
    return render(request,'myapp1/base.html')

@login_required
def informations(request):
    return render(request,'myapp1/informations.html')  

@login_required
def new_client(request):
    """Function create and store a new customer in the database """
   
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
    """ Class redact customer data"""
    model= Baza_client
    template_name = 'myapp1/new_client.html'
    form_class = Baza_client_Form

        
class LoginForm(LoginView):
    form_class = LoginUserForm
    template_name = 'myapp1/Login.html'
     

    def get_success_url(self) :
        return reverse_lazy ('home')
    
def logout_user(request):
    logout (request)
    return redirect('login') 

# class ApiListPaginations(PageNumberPagination):
#     page_size = 1
#     page_size_query_param = 'page_size'
#     max_page_size = 10000
    

class OrederViews(ModelViewSet, LoginRequiredMixin):
    """This class r"""
    queryset = Baza_client.objects.all()
    serializer_class = OrderSeriaLizer
    # permission_classes = [IsAuthenticated]
    # pagination_class = ApiListPaginations
    filter_backends= [DjangoFilterBackend, OrderingFilter , SearchFilter]
    filterset_fields = ['type_case', 'date', 'status_case', 'date_contract']
    ordering_fields = ['name_client', 'contract_number']
    search_fields = ['name_client', 'contract_number'] 

    def destroy (self, request, *args, **kwargs):
        client_del = self.get_object()
        client_del.delete()
        return  redirect('home')
        

class TypeViews(ModelViewSet):
    queryset = TypeCase.objects.all()
    serializer_class =  TypeCaseSeriaLizer

    def destro (self, request, *args, **kwargs):
        client_del = self.get_object()
        client_del.delete()
        return Response({'messsage' : "Clean"})

class StatusViews (ModelViewSet):
    queryset = StatusCase.objects.all()
    serializer_class =  StatusCaseSeriaLizer
    






   
   
 