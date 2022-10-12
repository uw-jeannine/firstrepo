import africastalking
from django.shortcuts import render
from .models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

username = "ndzphilbert@gmail.com"
api_key = "8ecbcc69d8b08589a210d71c8c3600daf48b3f8674b1b6a8e9dc741f0f41fc10"
africastalking.initialize(username,api_key)

# Create your views here.
def index(request):
    return render(request,'index.html')

def form(request):
    select = Registration.objects.all().order_by('id')
    contextdata ={
        'data' : select
    }
    return render(request,'form.html', context=contextdata)

def registration(request):
    select = Registration.objects.all().order_by('id')
    if request.method == 'POST':
        phonenumber = request.POST['phonenumber']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        insert = Registration(phone=phonenumber, firstname=firstname, lastname=lastname)
        try:
            insert.save()
            return render(request,'form.html',{'message':'Data has been inserted', 'data':select})
        except:
            return render(request,'form.htlm',{'message':'data not inserted', 'data':select})
    return render(request,'form.html')

def delete(request,id):
    select = Registration.objects.all().order_by('id')
    delete = Registration.objects.get(id=id).delete()
    return render(request,'form.html',{'del':'delete successfull', 'data':select})

def update(request,id):
    select = Registration.objects.all().order_by('id')
    updatedata = Registration.objects.get(id=id)
    if request.method == 'POST':
        updatedata.firstname = request.POST['firstname']
        updatedata.lastname = request.POST['lastname']
        updatedata.phone = request.POST['phonenumber']
        try:
            updatedata.save()
            return render(request,'updateform.html',{'messag':'Update successefull','data':select,'update':updatedata})
        except:
            return render(request,'updateform.html',{'messag':'Update successefull','data':select,'update':updatedata})
    return render(request,'updateform.html',{'update':updatedata, 'data':select})


def register(request):
    return render(request,'register.html')

def student(request):
    selectdata = Student.objects.all()
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        phone = request.POST['phonenumber']
        age = request.POST['age']
        insertdata = Student(firstname=fname, lastname=lname, phone=phone, age=age)
        try:
            insertdata.save()
            return render(request,'student.html',{'message':'Data sent, successfull','data':selectdata})
        except:
            return render(request, 'student.html',{'message':'Date sent, failed'})
    return render(request,'student.html',{'data':selectdata})

@csrf_exempt
def ussdapp(request):
    if request.method == 'POST':
        session_id = request.POST.get("sessionId", None)
        service_code = request.POST.get("serviceCode", None)
        phone_number = request.POST.get("phoneNumber", None)
        text = request.POST.get("text")
        # level = text.split('*')
        response =""
        # numb = text[:3]
        if text =='':
            response = "CON Welcome to ida technology USSD app \n "
            response +="1. Girls in code \n"
            response +="2. Sdf program "
        elif text =='1':
            response ="CON Welcome to Girls in code program "+str(len(level))+"\n"
            response +="1. Join the program \n"
            response +="2. checking registe\n"
            response +="3. Leave"
           #=========== Girls in =============
        elif text == '1*1':
            response ="CON Enter Your Fullname \n"
        elif text =='1*1' and int(len(level))== 2 and str(level[1]) in str(level):
            response ="CON Enter Your phone "
        elif text =='1*1' and int(len(level))== 3 and str(level[2]) in str(level):
            response ="CON Enter Your lastname "
        elif text =='1*1' and int(len(level))== 4 and str(level[3]) in str(level):
            fullname= str(level[1])
            phone= str(level[2])
            lastname = str(level[3])
            reg = Registration(phone=phone,firstname=fullname,lastname=lastname)
            save()
            response = "END Thank you for registering"
        else:
            response ="no choice "
        return HttpResponse(response)
    return HttpResponse('welcome')

def idaussd(request):
    if request.method == 'POST':
         session_id = request.values.get("sessionId", None)
         service_code = request.values.get("serviceCode", None)
         phone_number = request.values.get("phoneNumber", None)
         text = request.values.get("text", "default")
    return HttpResponse()