from django.shortcuts import render
from django.http import HttpResponse
from .models import school
from django.contrib.auth.models import  User,auth
from django.contrib import messages
def website(request):
    return render(request,"website.html")
def library(request):
    return render(request,"library.html")
def administration(request):
    return render(request,"administration.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def register(request):
    return render(request,"registration.html")





# Create your views here.

def registration(request):
    if request.method=='POST':
        username=request.POST.get('username')
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password1')
        confirm_password=request.POST.get('password2')
        if password==confirm_password:
              if User.objects.filter(username=username).exists():
                  messages.info(request,"username exist")
                  return redirect('reg')
              elif User.objects.filter(email=email).exists():
                 messages.info(request,'email exit')
                 return redirect('reg')
              else:
                reg_data=User.objects.create(username=username,email=email,first_name=firstname,last_name=lastname,password=password)


                reg_data.save()

        else:
            messages.info(request,"password dont match")
    return render(request,'registration.html')
'''def login(request):
    if request.method=='POST':
         username=request.POST.get('username')
         password=request.POST.get('password1')
         user=auth.authenticate(username=username,password=password)
         if user is not None:
              auth.login(request,user)
              return redirect("welcome")
         else:
             messages.info(request,"username password not match")
             return redirect("login")

    return render(request,'login.html')
def logout(request):
   auth.logout(request)
   return redirect("welcome")
def welcome(request):
 return render(request,'welcome.html')'''
