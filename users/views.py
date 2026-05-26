import gc
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from users.forms import UserRegistrationForm, HeartDataForm
from users.models import UserRegistrationModel, DataModel
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score
from django_pandas.io import read_frame
#%matplotlib inline
from sklearn.model_selection import train_test_split
from django.db.models import Q
import os
#print(os.listdir())
from django.http import HttpResponse
import warnings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import random
import string
import yagmail
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import pickle

def UserLogin(request):
    return render(request, 'UserLogin.html', {})


def UserRegisterAction(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            # return HttpResponseRedirect('./CustLogin')
            form = UserRegistrationForm()
            return render(request, 'Register.html', {'form': form})
        else:
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'Register.html', {'form': form})


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHomePage.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
            # return render(request, 'user/userpage.html',{})
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})




def UserAddData(request):
    if request.method == 'POST':
        form = HeartDataForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'Data Added Successfull')
            # return HttpResponseRedirect('./CustLogin')
            form = HeartDataForm()
            return render(request, 'users/UserAddData.html', {'form': form})
        else:
            print("Invalid form")
    else:
        form = HeartDataForm()
    return render(request, 'users/UserAddData.html', {'form': form})


def UserDataView(request):
    data_list = DataModel.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(data_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'users/DataView_list.html', {'users': users})

def UserDataView1(request):
    data_list = DataModel.objects.all()
    page = request.GET.get('page', 1)

    # paginator = Paginator(data_list, 10)
    # try:
    #     users = paginator.page(page)
    # except PageNotAnInteger:
    #     users = paginator.page(1)
    # except EmptyPage:
    #     users = paginator.page(paginator.num_pages)
    return render(request, 'users/DataView_list1.html', {'users': data_list})


def UserMachineLearning(request):
    pass

def predictt1(request):
    return render(request, "users/predict1.html")

# from pandas import read_csv
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# import pandas as pd

# import joblib
# import csv
# model = joblib.load("media/randomforest_model.sav")
# with open('media/Testing.csv', newline='') as f:
#         reader = csv.reader(f)
#         symptoms = next(reader)
#         symptoms = symptoms[:len(symptoms)-1]



# df = pd.read_csv(r'C:\Users\lenovo\Desktop\maternal test 1\media\Maternal Health Risk Data Set.csv')
df = pd.read_csv(r'/Users/user/Desktop/meternityapp/rar/media/Maternal Health Risk Data Set.csv')
#df = pd.read_csv(r'C:\Users\akbar\OneDrive\Desktop\meternityapp\rar\media\Maternal Health Risk Data Set.csv')
df = df.replace({'RiskLevel':{'low risk':0, 'mid risk':1 , 'high risk':2}})
X = df.drop(columns=['RiskLevel'],axis=1)
y = df['RiskLevel']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.1,stratify=y,random_state=2)
regressor = RandomForestRegressor(n_estimators=100)
regressor.fit(X_train,y_train)
test_data_prediction = regressor.predict(X_test)
classifier = RandomForestClassifier()
rfc=classifier.fit(X_train, y_train)
predictions = classifier.predict(X_test)
accuracy = accuracy_score(predictions, y_test)
pickle.dump(rfc, open('media/mra.pkl', 'wb'))

model = pickle.load(open('media/mra.pkl', 'rb'))

# def savedata(email,data1,data2,data3,data4,data5,data6):
#     try:
#         data_list = DataModel(email=email,data1=data1,data2=data2,data3=data3,data4=data4,data5=data5,data6=data6)
#         data_list.save()
#     except:
#         pass

def predictionss1(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        data1 = int(request.POST["field1"])
        data2 = int(request.POST["field2"]) 
        data3 = int(request.POST["field3"])
        data4 = float(request.POST["field4"])
        data5 = int(request.POST["field5"])
        data6 = int(request.POST["field6"])
        arr = np.array([[data1, data2, data3, data4,data5,data6]])
        pred = model.predict(arr)
        print(pred)
        print(email)
        data_list = DataModel(email=email,data1=data1,data2=data2,data3=data3,data4=data4,data5=data5,data6=data6, pred=pred)
        data_list.save()
        if pred == 0:
            try:
                user = 'maternalriskassement7@gmail.com'
                app_password = 'mietvkwoliqaswxj' # a token for gmail
                # to = 'akbarpasha0696@gmail.com'
                to = email
                subject = 'Maternal Risk Assessment'
                content = '''
                <p>Dear User,</p>
                <p>Thank you for using our service.</p>
                <p>Remember, it is crucial to consult your healthcare provider for 
                personalized advice and guidance tailored to your specific situation. 
                They will monitor your condition closely and provide the most appropriate care for you and your baby.
                </p>
                <p>Regards,</p>
                <p>Team Maternal Risk</p>
                </table>
                '''
                with yagmail.SMTP(user, app_password) as yag:
                    yag.send(to, subject, content)
                    print('Sent email successfully')
                    messages.success(request, 'You are at low risk')
                    return render(request, 'users/predict1.html',{'dataa2': data2, 'dataa3': data3, 'dataa5':data5})
            except:
                pass
            
        elif pred == 1:
            try:
                user = 'maternalriskassement7@gmail.com'
                app_password = 'mietvkwoliqaswxj' # a token for gmail
                # to = 'akbarpasha0696@gmail.com'
                to = email
                subject = 'Maternal Risk Assessment'
                content = '''
                <p>Dear User,</p>
                <p>Thank you for using our service.</p>
                <p>Remember, it is crucial to consult your healthcare provider for 
                personalized advice and guidance tailored to your specific situation. 
                They will monitor your condition closely and provide the most appropriate care for you and your baby.
                </p>
                <p>Regards,</p>
                <p>Team Maternal Risk</p>
                </table>
                '''
                with yagmail.SMTP(user, app_password) as yag:
                    yag.send(to, subject, content)
                    print('Sent email successfully')
                    messages.success(request, 'You are at mid risk')
                    return render(request, 'users/predict1.html',{'dataa2': data2, 'dataa3': data3, 'dataa5':data5})
            except:
                pass
        elif pred == 2:
            try:
                user = 'maternalriskassement7@gmail.com'
                app_password = 'mietvkwoliqaswxj' # a token for gmail
                # to = 'akbarpasha0696@gmail.com'
                to = email
                subject = 'Maternal Risk Assessment'
                content = '''
                <p>Dear User,</p>
                <p>Thank you for using our service.</p>
                <p>Remember, it is crucial to consult your healthcare provider for 
                personalized advice and guidance tailored to your specific situation. 
                They will monitor your condition closely and provide the most appropriate care for you and your baby.
                </p>
                <p>Regards,</p>
                <p>Team Maternal Risk</p>
                </table>
                '''
                with yagmail.SMTP(user, app_password) as yag:
                    yag.send(to, subject, content)
                    print('Sent email successfully')
                    
                    messages.success(request, 'You are at high risk')
                    return render(request, 'users/predict1.html',{'dataa2': data2, 'dataa3': data3, 'dataa5':data5})
            except:
                pass
    return render(request, 'users/predict1.html')

def idsearch(request):
    email = request.POST['email']
    print(email)

    data = DataModel.objects.filter(email=email)
    print("naresh")

    return render(request, 'users/search.html', {'idata':data})



try:
        user = 'velishalaganesh3@gmail.com'
        app_password = 'dgnugyumwxrucxbi' # a token for gmail
        # to = 'akbarpasha0696@gmail.com'
        to = '218r1a04c4@gmail.com'
        subject = 'AI Based survelanace for detection of vehicles with out helment'
        content = '''
        <p>Dear User,</p>
        <p>Thank you for using our service.</p>
        <p>you have done the trffic voilation with {license_plate}  so kindly pay the challan  1000 rupees
        </p>
        <p>Regards,</p>
        <p>Team Traffic Department</p>
        </table>
        '''
        with yagmail.SMTP(user, app_password) as yag:
            yag.send(to, subject, content)
            print('Sent email successfully')
            
except:
    pass