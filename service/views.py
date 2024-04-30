from django.shortcuts import render, redirect
from service.models import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.utils import timezone
from django.http import HttpResponseRedirect



# Create your views here.

def submit(request):
    if request.method == "POST":
        a=request.POST.get('name')
        b=request.POST.get('phone')
        c=request.POST.get('address')
        d=request.POST.get('request_type')
        e=request.POST.get('details')
        f=request.POST.get('attachment')
        info = service_request(name = a, phone = b, address = c, request_type = d, details = e, attachment = f )
        info.save() 
        
        messages.success (request, 'Request for sucessfully submited')
  
    return render(request, 'service.html')


def account_info(request):
    info = service_request.objects.all()
    dict1 = {'information': info}   
    
    
    
    return render(request, 'info.html', dict1)


def status(request):
    info = service_request.objects.all()
    dict1 = {'information': info}
    
    return render(request, 'status.html', dict1)

def login_user(request):
    if request.method == "POST":
        a = request.POST.get('username')
        b = request.POST.get('password')
        
        user = authenticate(request, username = a , password = b) 
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,"You are write incorrect password")
              
    
    
    return render(request, 'login.html')


def dashboard(request):
    return render(request,'dashboard/index.html')

def user_info(request):
    return render(request, 'dashboard/tables.html')

def customer_details(request):
    info = service_request.objects.all()
    dict1 = {'information': info}
    
    return render(request,'dashboard/tables.html', dict1)

def delete_record(request, id):
    if request.method == 'POST':
        data = service_request.objects.get(pk=id)
        data.delete()
    return HttpResponseRedirect('/customer-detail')

def edit_record(request, id):
    info= service_request.objects.filter(pk=id)
    data = {'information':info}
    return render(request,'dashboard/editrecord.html', data)


def update_record(request, id):
    info = service_request.objects.get(pk=id)
    
    info.name = request.POST.get('name')
    info.status = request.POST.get('status')
    info.phone = request.POST.get('phone')
    info.details = request.POST.get('details')
    if info.status == 'Resolved':
        info.resolved_at = timezone.now()
    else:
        info.resolved_at = None

    info.save()
    return HttpResponseRedirect('/customer-detail')



    

    
 
