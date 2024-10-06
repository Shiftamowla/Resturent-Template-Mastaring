from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from myapp.models import *

def loginpage(req):
    if req.method=='POST':
        username=req.POST.get('username')
        password = req.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            login (req,user)
            return redirect('dashboard')


    return render(req, 'login.html')

def registerpage(req):
    if req.method=='POST':
        username=req.POST.get('username')
        email=req.POST.get('email')
        password = req.POST.get('password')
        Confirm_Password=req.POST.get('Confirm_Password')

        if password==Confirm_Password:
            user=User.objects.create_user(username=username,email=email,password=Confirm_Password)
            return redirect('loginpage')

        else:
            return HttpResponse('Password not Matched')


    return render(req, 'register.html')

def homepage(req):
    return render(req,'home.html')
def home(req):
    return render(req,'h.html')

def about(req):
    return render(req,'about.html')

def menu(req):
    return render(req,'menu.html')

def event(req):
    return render(req,'event.html')



def logoutpage(req):
    logout(req)
    return redirect('homepage')

def base(req):
    return render(req,'base.html')

@login_required
def dashboard(req):
    return render(req,'dashboard.html')

def contact(req):
    return render(req,'contact.html')

def chef(req):
    data=Chefmodel.objects.all()
    return render(req,'chef.html',{'data':data})

def addchef(req):
    if req. method=='POST':
        Name=req.POST.get('Name')
        Chef=req.POST.get('Chef')
        Description=req.POST.get('Description')
        img=req.FILES.get('img')

        c=Chefmodel(
            Name=Name,
            Chef=Chef,
            Description=Description,
            img=img,
        )
        c.save()
        return redirect('chef')
    
    return render(req,'addchef.html')
def edit(req,id):
    data=Chefmodel.objects.filter(id=id)
    return render(req,'edit.html',{'data':data})

def update(req):
    if req. method=='POST':
        id=req.POST.get('id')
        Name=req.POST.get('Name')
        Chef=req.POST.get('Chef')
        Description=req.POST.get('Description')
        img=req.FILES.get('img')

        c=Chefmodel(
            id=id,
            Name=Name,
            Chef=Chef,
            Description=Description,
            img=img,
        )
        if img:
            c.img=img
        c.save()
    
    return redirect('chef')

def delete(req,id):
    data=Chefmodel.objects.filter(id=id)
    data.delete()
    return redirect('chef')

def menu(req):
    data=Menumodel.objects.all()
    return render(req,'menu.html',{'data':data})

def addmenu(req):
    if req. method=='POST':
        Name=req.POST.get('Name')
        Price=req.POST.get('Price')
        Description=req.POST.get('Description')
        img=req.FILES.get('img')

        c=Menumodel(
            Name=Name,
            Price=Price,
            Description=Description,
            img=img,
        )
        c.save()
        return redirect('menu')
    
    return render(req,'addmenu.html')
def editmenu(req,id):
    data=Menumodel.objects.filter(id=id)
    return render(req,'editmenu.html',{'data':data})

def updatemenu(req):
    if req. method=='POST':
        id=req.POST.get('id')
        Name=req.POST.get('Name')
        Price=req.POST.get('Price')
        Description=req.POST.get('Description')
        img=req.FILES.get('img')

        c=Menumodel(
            id=id,
            Name=Name,
            Price=Price,
            Description=Description,
            img=img,
        )
        if img:
            c.img=img
        c.save()
    
    return redirect('menu')

def deletemenu(req,id):
    data=Menumodel.objects.filter(id=id)
    data.delete()
    return redirect('menu')


