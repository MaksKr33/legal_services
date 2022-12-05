from django.urls import path
from myapp1.views import OrederViews, TypeViews, StatusViews, UpdateClients, LoginForm, TypeViews
from myapp1.views import  base, informations, new_client, logout_user
from rest_framework.routers import SimpleRouter 

router =  SimpleRouter()
router.register('client',  OrederViews)
router.register('typecase',  TypeViews)
router.register('statuscase', StatusViews )

urlpatterns = [
        path('', base, name= 'home'),
        path('about', new_client , name= 'client'),
        path('info', informations , name= 'info_page'),
        path('login', LoginForm.as_view() , name= 'login'),
        path('logout', logout_user , name= 'logout'),
        path('<int:pk>/update/', UpdateClients.as_view(), name= 'update_client'),
        path('client/<int:pk>', OrederViews.as_view({'get': 'destroy'}), name='delete' ),
      
       ]

urlpatterns+=router.urls