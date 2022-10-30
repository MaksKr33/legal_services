

from django.urls import path
from myapp1.views import OrederViews,TypeViews, StatusViews, UpdateClients, contact_new,   base , informations, new_client

from rest_framework.routers import SimpleRouter

router =  SimpleRouter()
router.register('client',  OrederViews)
router.register('typecase',  TypeViews)
router.register('statuscase', StatusViews )

urlpatterns = [
        path('', base, name= 'home'),
        path('about', new_client , name= 'client'),
        path('info', informations , name= 'info_page'),
        path('contact', contact_new, name= 'contakt_client'),
        path('about/<int:pk>/update', UpdateClients.as_view(), name= 'update_client')
       
] 




urlpatterns+=router.urls