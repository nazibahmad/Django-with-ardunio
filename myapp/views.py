from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, Group, Permission
from django.views.generic import RedirectView
from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponseRedirect
import serial


 
def dashboard(request):
  ser = serial.Serial("COM6", 9600)
  while True:
  
     u=ser.readline()
     return render(request, 'myapp/dash.html',{'u':u})
   
