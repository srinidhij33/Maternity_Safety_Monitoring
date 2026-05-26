from django.shortcuts import render
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
from django.contrib import messages
import yagmail

def index(request):
    return render(request,'index.html',{})


def logout(request):
    return render(request,'index.html',{})

def scheme(request):
    return render(request,'scheme.html',{})

def predictt(request):
    return render(request, "users/predict160.html")

# df = pd.read_csv(r'C:\Users\lenovo\Desktop\maternal test 1\media\Maternal Health Risk Data Set.csv')
df = pd.read_csv(r'/Users/user/Desktop/meternityapp/rar/media/Maternal Health Risk Data Set.csv')
# df = pd.read_csv(r'C:\Users\akbar\OneDrive\Desktop\meternityapp\rar\media\Maternal Health Risk Data Set.csv')
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

def predictionsss(request):
    
    if request.method == 'POST':
        # email = request.POST['email']
        data1 = int(request.POST["field1"])
        data2 = int(request.POST["field2"]) 
        data3 = int(request.POST["field3"])
        data4 = float(request.POST["field4"])
        data5 = int(request.POST["field5"])
        data6 = int(request.POST["field6"])
        arr = np.array([[data1, data2, data3, data4,data5,data6]])
        pred = model.predict(arr)
        print(pred)

        if pred == 0:
            messages.success(request, 'You are at low risk')
            return render(request, 'users/predict.html', {"data2":data2,"data3":data3,"data5":data5})
        elif pred == 1:

            messages.success(request, 'You are at mid risk')
            return render(request, 'users/predict.html',{"data2":data2,"data3":data3,"data5":data5})

        elif pred == 2:
            messages.success(request, 'You are at high risk')
            return render(request, 'users/predict.html',{"data2":data2,"data3":data3,"data5":data5})
    return render(request, 'users/predict.html')

def after(request):
    return render(request,'after.html',{})


def predictionss(request):
    if request.method == 'POST':
        # email = request.POST['email']
        data1 = int(request.POST["field1"])
        data2 = int(request.POST["field2"])
        data3 = int(request.POST["field3"])
        data4 = float(request.POST["field4"])
        data5 = int(request.POST["field5"])
        data6 = int(request.POST["field6"])
        arr = np.array([[data1, data2, data3, data4, data5, data6]])
        pred = model.predict(arr)
        print(pred)
        if pred == 0:

            messages.success(request, 'You are at low risk')
            return render(request, 'users/predict.html',{'dataa2': data2, 'dataa3': data3, 'dataa5':data5})
        elif pred == 1:

            messages.success(request, 'You are at mid risk')
            return render(request, 'users/predict.html',{'dataa2': data2, 'dataa3': data3, 'dataa5':data5})

        elif pred == 2:
            messages.success(request, 'You are at high risk')
            return render(request, 'users/predict.html', {'dataa2': data2, 'dataa3': data3, 'dataa5':data5})
    return render(request, 'users/predict.html')