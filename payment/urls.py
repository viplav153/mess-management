from django.urls import path

from . import views

urlpatterns = [
    path('payment', views.payment, name='payment'),
    path('thalii', views.thalii, name='thalii'),
    path('info', views.info, name='info'),
    path('cancel', views.cancel, name='cancel'),

]
