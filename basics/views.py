from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from sklearn.model_selection import train_test_split
import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image
from django.contrib.auth import authenticate,login,logout


# Create your views here.


def userlogin(request):
    if request.method=="POST":
        data=request.POST
        username = data.get('textusername')
        password=data.get('textpassword')
        user= User.objects.filter(username=username)
        if not user.exists():
            result="Invalid username"
            return render(request,'login.html',context={'result':result}) 
        user= authenticate(username=username,password=password)
        if(user is None):
            result="Invalid password"
            return render(request,'login.html',context={'result':result})
        else:
            login(request,user)
            return redirect('/donor/') 
    return render(request,'login.html') 


def userlogout(request):
    logout(request)
    return redirect('/userlogin')

def register(request): 
    if(request.method=="POST"):
        data= request.POST
        firstname = data.get('textfirstname')
        lastname=data.get('textlastname')
        username=data.get('textusername')
        password= data.get('textpassword')
        user=User.objects.filter(username=username)
        if(user.exists()):
            result="User name already exists"
            return render(request,'register.html',context={'result':result})

        if('submit' in request.POST ):
            user= User.objects.create(first_name=firstname,last_name=lastname,username=username)
            user.set_password(password)
            user.save()
            result="Registered successfully"
            return render(request,'register.html',context={'result':result})     
    return render(request,'register.html')

def donor(request):
    return render(request,'donor.html')

def home(request):
    return render(request,'home.html')

def persondetails(request):
    if(request.method=="POST"):
        data=request.POST
        personname = data.get('textpername')
        phonenumber = data.get('textphoneno')
        emailid=data.get('textperemail')
        personaddress = data.get('textperaddress')
        persondob = data.get('textperdob')
        bloodgroupname = data.get('textbloodgroupname')
        PersonDetails.objects.create(PER_NAME=personname,PER_PHONENO=phonenumber,PER_EMAIL=emailid,PER_ADDRESS=personaddress,PER_DOB=persondob,PER_BLOODGROUPNAME=bloodgroupname)
        result="Person details saved successfully";
        return render(request,'persondetails.html',context={'result':result})
    return render(request,'persondetails.html')


def bloodgroup(request):
    if(request.method=="POST"):
        data=request.POST
        bloodgroupname = data.get('textbloodgroupname')
        bloodgroupdesc = data.get('textbloodgroupdesc')
        BloodGroup.objects.create(BLOOD_GROUPNAME=bloodgroupname,BLOOD_GROUPDESC=bloodgroupdesc)
        result="Blood Group details saved successfully";
        return render(request,'bloodgroup.html',context={'result':result})
    return render(request,'bloodgroup.html')


def donateblood(request):
    if(request.method=="POST"):
        data=request.POST
        donorname = data.get('textdonorname')
        bloodgroupname = data.get('textbloodgroupname')
        donordate = data.get('textdonordate')
        donorqty = data.get('textdonorqty')
        DonateBlood.objects.create(DONOR_NAME=donorname,DONOR_BLOODGROUPNAME=bloodgroupname,DONOR_DATE=donordate,DONOR_QTY=donorqty)
        result="Blood Donated successfully";
        return render(request,'donateblood.html',context={'result':result})
    return render(request,'donateblood.html')


def dementia(request):
    if request.method == 'POST':
        data = request.POST
        SubjectID = data.get('textsubject',0)
        mridid = data.get('textmri',0)
        Visit = data.get('textvisit',0)
        MRDelay = data.get('texttextmrdelay',0)
        Malefemale = data.get('texttextmf',0)
        hand = data.get('texthand',0)
        Age = data.get('textage',0)
        educ = data.get('textedu',0)
        Ses = data.get('textses',0)
        mmse = data.get('textmmse',0)
        cdr = data.get('textcdr',0)
        eTIV = data.get('textetiv',0)
        nWBV = data.get('textnwbv',0)
        asf = data.get('textasf',0)
        if 'buttonpredict' in request.POST:
            import pandas as pd
            path="C:\\Users\\nites\\OneDrive\\Desktop\\internship\\2024_projects\\2024_projects\\21_dementiadiseasetypeprediction\\dementia_dataset.csv"
            data=pd.read_csv(path)
            medianavl=data.SES.median()
            data.SES=data.SES.fillna(medianavl)
            medianavl=data.MMSE.median()
            data.MMSE=data.MMSE.fillna(medianavl)
            data['M/F']=data['M/F'].map({'M':1,'F':0})
            data['Group']=data['Group'].map({'Demented':1,'Nondemented':0,'Converted':2})
            import sklearn
            from sklearn.preprocessing import LabelEncoder
            le_SubjectID=LabelEncoder()
            le_MRIID=LabelEncoder()
            le_Hand=LabelEncoder()
            data['Subject ID']=le_SubjectID.fit_transform(data['Subject ID'])#adding column
            data['MRI ID']=le_MRIID.fit_transform(data['MRI ID'])
            data['Hand']=le_Hand.fit_transform(data['Hand'])
            inputs=data.drop(['Group'],axis=1)
            output=data['Group']
            import sklearn
            from sklearn.model_selection import train_test_split
            x_train,x_test,y_train,y_test=train_test_split(inputs,output,test_size=0.2)
            from sklearn.preprocessing import StandardScaler
            sc=StandardScaler()
            x_train=sc.fit_transform(x_train)
            x_test=sc.transform(x_test)
            from sklearn.svm import SVC
            model=SVC()
            model.fit(x_train,y_train)
            y_pred=model.predict(x_test)
            from sklearn.metrics import confusion_matrix
            cm=confusion_matrix(y_test,y_pred) #compare
            model.fit(inputs, output)
            result = model.predict([[float(SubjectID),float(mridid),int(Visit),int(MRDelay),str(Malefemale),str(hand), int(Age),int(educ),float(Ses),float(mmse),float(cdr),int(eTIV),float(nWBV),float(asf)]])
            if result == 1:
                result = "Non demented"
            elif result == 0:
                result = "Demented"
            else:
                result = "Converted"        
            return render(request,'dementia.html',context={'result':"dementia :"+str(result)})
    return render(request, 'dementia.html')



def demo(request):
    return render(request,'demo.html')

def persondetailsview(request):
    result= PersonDetails.objects.all()
    return render(request,'persondetailsview.html',context={'result':result})

def persondetailsupdate(request,id):
    result=PersonDetails.objects.get(id=id) #columnname=value  
    if(request.method=="POST"):
        data=request.POST
        personname = data.get('textpername')
        phonenumber = data.get('textphoneno')
        emailid=data.get('textperemail')
        personaddress = data.get('textperaddress')
        persondob = data.get('textperdob')
        bloodgroupname = data.get('textbloodgroupname')
        result.PER_NAME= pername
        result.PER_PHONENO = perphoneno
        result.PER_EMAIL= peremail
        result.PER_ADDRESS= peraddress
        result.PER_DOB= perdob
        result.PER_BLOODGROUPNAME= perbloodgroupname
        result.save()        
    return redirect('/persondetailsview/')
    return render(request,'persondetailsupdate.html',context={'result':result})