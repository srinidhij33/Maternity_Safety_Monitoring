from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from users.models import UserRegistrationModel, HeartDataModel
from doctor.models import doctorModel
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score
from django_pandas.io import read_frame
#%matplotlib inline
from sklearn.model_selection import train_test_split
import os
#print(os.listdir())

import warnings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def AdminLogin(request):
    return render(request,'AdminLogin.html',{})


def AdminLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("User ID is = ", usrid)
        if usrid == 'admin' and pswd == 'admin':
            return render(request, 'admins/AdminHome.html')

        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'AdminLogin.html',{})


def RegisterUsersView(request):
    data = UserRegistrationModel.objects.all()
    return render(request,'admins/ViewRegisterUsers.html',{'data':data})

def doctordetails(request):
    qs=doctorModel.objects.all()
    return render(request,'admins/doctordetails.html',{"object":qs})


def ActivaUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id, status)
        UserRegistrationModel.objects.filter(id=id).update(status=status)
        data = UserRegistrationModel.objects.all()
        return render(request,'admins/ViewRegisterUsers.html',{'data':data})

def activatedoctor(request):
    if request.method == 'GET':
        uname = request.GET.get('pid')
        print(uname)
        status = 'Activated'
        print("pid=", uname, "status=", status)
        doctorModel.objects.filter(id=uname).update(status=status)
        qs = doctorModel.objects.all()
        return render(request,"admins/doctordetails.html", {"object": qs})

def adminML(request):
    pass