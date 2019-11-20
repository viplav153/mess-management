from django.shortcuts import render
from .models import Menu
from django.shortcuts import render, redirect

# Create your views here.



def menu(request):
    menus=Menu.objects.all()
    return render(request, 'menus/Menu.html',{'menus':menus})
