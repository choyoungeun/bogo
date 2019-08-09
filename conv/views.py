from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
from django.utils import timezone

def intro(request):
    return render(request,'intro.html')

def home(request):
    return render(request,'home.html')

def gs25(request):
    items=Product.objects
    item_list=Product.objects.all().order_by('-id')
    paginator=Paginator(item_list,12)
    page=request.GET.get('page')
    posts=paginator.get_page(page)

    return render(request,'gs25.html',{'items':items,'posts':posts})

def seven(request):
    items=Product.objects
    item_list=Product.objects.all().order_by('-id')
    paginator=Paginator(item_list,12)
    page=request.GET.get('page')
    posts=paginator.get_page(page)

    return render(request,'seven.html',{'items':items,'posts':posts})

def emart(request):
    items=Product.objects
    item_list=Product.objects.all().order_by('-id')
    paginator=Paginator(item_list,12)
    page=request.GET.get('page')
    posts=paginator.get_page(page)

    return render(request,'emart.html',{'items':items,'posts':posts})
    
def ministop(request):
    items=Product.objects
    item_list=Product.objects.all().order_by('-id')
    paginator=Paginator(item_list,12)
    page=request.GET.get('page')
    posts=paginator.get_page(page)

    return render(request,'ministop.html',{'items':items,'posts':posts})
    
def cu(request):
    items=Product.objects
    item_list=Product.objects.all().order_by('-id')
    paginator=Paginator(item_list,12)
    page=request.GET.get('page')
    posts=paginator.get_page(page)

    return render(request,'cu.html',{'items':items,'posts':posts})
