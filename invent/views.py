from django.shortcuts import render,redirect

from invent.models import Laptop,Desktop,Mobile
from . import models
from django.views import View
from .forms import DesktopForm,LaptopForm,MobileForm
# Create your views here.
def index(request):

    return render(request,'invent/index.html')
def  display_laptops(request):

    laptops = models.Laptop.objects.all()
    #print(laptops)
    context = {'products':laptops,'header':'Laptop'}
    return render(request,'invent/index.html',context)

def  display_desktops(request):
    desktops = models.Desktop.objects.all()
    context = {'products':desktops,'header':'Desktop'}
    return render(request,'invent/index.html',context)

def  display_mobiles(request):
    mobiles = models.Mobile.objects.all()
    context = {'products':mobiles,'header':'Mobile'}
    return render(request,'invent/index.html',context)

def add_device(request,cls):
    if request.method == 'POST':
        print('post')

        form = cls(request.POST,request.FILES)
        if form.is_valid():
           print('post2')
           form.save()
           return redirect('index')


    else:
       form = cls()
       print('not post')
    return render(request,'invent/add_device.html',{'form':form})

def add_laptop(request):
    return add_device(request,LaptopForm)
def add_desktop(request):
    return add_device(request,DesktopForm)
def add_mobile(request):
    return add_device(request,MobileForm)


def delete_item(request,prod_id,class_name):
    item = class_name.objects.get(id=prod_id)
    item.delete()
    return redirect('index')
def delete_laptop(request,prod_id):
    return delete_item(request,prod_id,Laptop)
def delete_desktop(request,prod_id):
    return delete_item(request,prod_id,Desktop)
def delete_mobile(request,prod_id):
    return delete_item(request,prod_id,Mobile)

def Edit_item(request,prod_id,class_name,classform):
    item = class_name.objects.get(id=prod_id)
    if request.method == 'POST':
        form = classform(request.POST, request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = classform(instance=item)
    return render(request, 'invent/edit.html', {'form':form,'item':item,})

def edit_Laptop(request,prod_id):
    return Edit_item(request,prod_id,Laptop,LaptopForm)

def edit_Desktop(request,prod_id):
    return Edit_item(request,prod_id,Desktop,DesktopForm)

def edit_Mobile(request,prod_id):
    return Edit_item(request,prod_id,Mobile,MobileForm)

