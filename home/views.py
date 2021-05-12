from django.shortcuts import render ,HttpResponse ,redirect
from home.models import patient_data 
from datetime import datetime
from .models import patient_data
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 

def hosp(request):
    context={}
    return render (request,'hosp.html')

def handlelogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render (request,'hosp.html')
    else:
        return render (request,'index.html')
    
    return render (request,'index.html')

def handlelogout(request):
    context={}
    return render (request,'hosp.html')



def index(request):
    if request.method == 'GET':
        return render (request,'index.html')

    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render (request,'hosp.html')
            
        else:
            return render (request,'index.html')
   
    

   
def branch(request):
    context={}
    return render (request,'branch.html')
 
   
def add_data(request):
   
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        date_adm = request.POST.get('date_adm')
        diagnosis = request.POST.get('diagnosis')
        prescription = request.POST.get('prescription')
        nok_add = request.POST.get('address')
        hosp_name = request.POST.get('hosp_name')
        ward = request.POST.get('ward')
        patientData = patient_data (
            patient_id = patient_id,
            gender = gender,
            age = age,
            date_adm = date_adm,
            diagnosis = diagnosis,
            prescription = prescription,
            nok_add = nok_add,
            hosp_name = hosp_name,
            ward = ward,
         )
        patientData.save()
    context={}

    return render (request,'add_data.html')

  
def show_data(request):
    if request.method == 'POST':
        pat_id = request.POST.get('pat_id')
        obj = patient_data.objects.get(patient_id=pat_id)
        context = {
        'patient_id': obj.patient_id,
        'gender' : obj.gender,
        'age' : obj.age,
        'date_adm' : obj.date_adm,
        'diagnosis': obj.diagnosis,
        'prescription' : obj.prescription,
        'nok_add' : obj.nok_add,
        'hosp_name' :obj.hosp_name,
        'ward'  : obj.ward,
    }
    return render (request,'show_data.html',context)

def show_database(request):
    patients = patient_data.objects.all()
    return render (request,'show_database.html',{'patients':patients})

    # context = {
    #     'patient_id': obj.patient_id,
    #     'gender' : obj.gender,
    #     'age' : obj.age,
    #     'date_adm' : obj.date_adm,
    #     'diagnosis': obj.diagnosis,
    #     'prescription' : obj.prescription,
    #     'nok_add' : obj.nok_add,
    #     'hosp_name' :obj.hosp_name,
    #     'ward'  : obj.ward,
    # }
  
   


     
