from django.urls import path
from django.contrib import admin
import testApp.views as views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
path('create',views.create,name='create'),
path('create_product',views.create_product,name='create_product'),
path('get_product',views.get_product,name='get_product'),
path('create_user',views.create_user,name='create_user'),
path('login',views.login,name='login'),
path('get_user',views.get_user,name='get_user'),
path('create_card',views.create_card,name='create_card'),
path('get_card',views.get_card,name='get_card'),
path('del_card',views.del_card,name='del_card'),
path('create_address',views.create_address,name='create_address'),
path('get_address',views.get_address,name='get_address')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)