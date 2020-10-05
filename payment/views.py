from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms import ProfileUpadteForm
from .models import Payment


# Create your views here.
@login_required(login_url="/accounts/login")
# NIKHIL plzz add here

# Aakash paste here

@login_required
def thalii(request):
    p_form = ProfileUpadteForm(instance=request.user.profile)
    if request.method == 'POST':
        a = Payment.objects.get(user=request.user)
        a.thali -= 1
        a.amount = (a.amount) - 50
        a.save()

        return redirect('/payment/thalii')
    else:
        return render(request, 'accounts/profile.html', {'p_form': p_form})


@login_required
def thalii(request):
    p_form = ProfileUpadteForm(instance=request.user.profile)
    if request.method == 'POST':
        a = Payment.objects.get(user=request.user)
        a.thali -= 1
        a.amount = (a.amount) - 50
        a.save()

        return redirect('/payment/thalii')
    else:
        return render(request, 'accounts/profile.html', {'p_form': p_form})


# kushagra plzz add here


# pratham plzz paste below here
@login_required
def cancel(request):
    if request.method == 'POST':
        a = Payment.objects.get(user=request.user)
        a.thali -= (a.subs) * 60
        a.amount = (a.amount) - (a.subs) * 3000
        a.save()
        messages.success(request, f'Oops you cancelled your request')
        return redirect('/payment/payment')
    else:
        return render(request, 'payment/payment.html', )
