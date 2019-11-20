from django.urls import path,include
from django.contrib.auth import views as auth_views
from .import views

urlpatterns=[
path('payment',views.payment,name='payment'),
path('thalii',views.thalii,name='thalii'),
path('info',views.info,name='info'),
path('cancel',views.cancel,name='cancel'),




]