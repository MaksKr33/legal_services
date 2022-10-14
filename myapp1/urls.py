from django.urls import path
from myapp1.views import OrederViews, contact_new, new_client ,  base

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('client',  OrederViews)

urlpatterns = [
        path('', base, name= 'home'),
        path('about', new_client, name= 'client'),
        # path('contact', contact, name= 'contakt_client')
        path('contact', contact_new, name= 'contakt_client')
] 

urlpatterns+=router.urls