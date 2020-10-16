from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from accounts.forms import ProfileUpadteForm
from .models import Payment,Info
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q

# Create your views here.
@login_required(login_url="/accounts/login")
def payment(request):
    infos= Info.objects.filter(subscribed_by=request.user).order_by('-pub_date')
    
    
    
    if request.method == 'POST':
        try:
            if(int(request.POST['subs'])<=12):
                a=Payment.objects.get(user=request.user)
        
                a.subs = int(request.POST['subs'])
                a.amount = a.amount + (a.subs)*3000
                a.thali=   a.thali + (a.subs)*60
            
                a.pub_date = timezone.datetime.now()
                messages.success(request,f'please take cash  {(a.subs)*3000}!!')
        
                a.save()
                return render(request,'payment/maintain.html')
            else:
                messages.success(request,f'please input months less than 12 !!')
                return render(request, 'payment/payment.html',{'infos':infos})

            
            
        except ObjectDoesNotExist:
            b=Payment()
            b.user=request.user
            b.subs = int(request.POST['subs'])
            b.amount = b.amount + (b.subs)*3000
            b.thali=   b.thali + (b.subs)*60
            
            b.pub_date = timezone.datetime.now()
            messages.success(request,f'please take cash{(b.subs)*3000}!!')
            b.save()
            return render(request,'payment/maintain.html')
    else:
        paginator = Paginator(infos, 3) # Show 3 object per page
        page = request.GET.get('page')
        infos = paginator.get_page(page)
        return render(request, 'payment/payment.html',{'infos':infos})


            
            

            
@login_required
def thalii(request):
    p_form=ProfileUpadteForm(instance=request.user.profile)
    if request.method =='POST' :
        a=Payment.objects.get(user=request.user)
        a.thali-=1
        a.amount=(a.amount)-50
        a.save()

        return redirect('/payment/thalii')
    else:
        return render(request,'accounts/profile.html',{'p_form':p_form})


@login_required
def info(request):
    infos= Info.objects.filter(subscribed_by=request.user).order_by('-pub_date')
   
    
    if request.method == 'POST':
        
       
        a= Payment.objects.get(user=request.user)
        inf=Info()
        inf.subs=a.subs
            
        inf.pub_date = timezone.datetime.now()
        inf.subscribed_by = request.user
        messages.success(request,f'Your meal is successfully updated!!')
        inf.save()
            
        return redirect('/payment/payment')
       

    else:
        paginator = Paginator(infos, 3) # Show 3 object per page
        page = request.GET.get('page')
        infos = paginator.get_page(page)
        return render(request, 'payment/payment.html',{'infos':infos})

@login_required
def cancel(request):
   
    if request.method =='POST' :
        a=Payment.objects.get(user=request.user)
        a.thali-=(a.subs)*60
        a.amount=(a.amount)- (a.subs)*3000
        a.save()
        messages.success(request,f'Oops you cancelled your request')
        return redirect('/payment/payment')
    else:
        return render(request,'payment/payment.html',)
   
