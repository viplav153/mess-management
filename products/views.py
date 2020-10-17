from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages

def home(request):
    products = Product.objects
    return render(request, 'products/home.html',{'products':products})
def addmeUp():
    return 6+7

#aakash paste your code here
@login_required(login_url="/accounts/signup")
def create(request):
    products = Product.objects.all().order_by('-pub_date')
   
    
    if request.method == 'POST':
        
        if request.POST['title'] and request.POST['body'] and request.POST['url'] :
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            product.url = request.POST['url']
            
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            messages.success(request,f'Your feedback has been saved !!')
            product.save()
            
            return redirect('create')
        else:
            return render(request, 'products/create.html',{'error':'All fields are required.'})
    else:
        paginator = Paginator(products, 3) # Show 5 object per page
        page = request.GET.get('page')
        products = paginator.get_page(page)
        return render(request, 'products/create.html',{'products':products})



def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html',{'product':product})

@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/' + str(product.id))
