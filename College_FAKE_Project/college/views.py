from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from faker import Faker 

fake = Faker()
from .models import CollegeDate

def home(request):
    return render(request,'COLLEGE/home.html')

def college_names_view(request):
    for i in range(3):
        first_name = fake.first_name()
        last_name = fake.last_name()
        username = fake.random_element(elements=("DJANGO-ADi","NARAYANA-SIR","SRINIVAS-SIR","RATNAKUMAR-SIR"))
        mobile = fake.random_int(min=9398520750,max=9999635699)
        email = fake.email()
        college = fake.random_element(elements=("VIKRMA SHIMHAPURI UNIVERSITY","YOGI VEMUNA UNIVERSITY","SVU","MAHARSTA UNIVERSITY","DELHI UNIVERSITY"))
        city = fake.city()
        fees = fake.random_int(min=136500,max=256325)
        admisin_no = fake.random_element(elements=("abcd125631","fjdshf541","hdu23514","yhht23144","gwurg44112"))


        data = CollegeDate(first_name=first_name,last_name=last_name,username=username,email=email,mobile=mobile,college=college,city=city,fees=fees,addmision_numbers=admisin_no)

        data.save()

    return render(request,'COLLEGE/newadd.html')

def College_display_data(request):
    if request.method == "POST":
        username = request.POST.get('one')
      
        return render(request,'COLLEGE/College_display_data_view.html',{'college':username})
    else:

        college = CollegeDate.objects.all()
    
    context = {
    'dispaly_college' : college

    }

    print(college)
    return render(request,'COLLEGE/College_display_data_view.html',context)


def vsu_view(request):
    vsu = CollegeDate.objects.filter(college='VIKRMA SHIMHAPURI UNIVERSITY')
    context = {
        'vsu':vsu
    }
    return render(request,'COLLEGE/vsu.html',context)


def yvu_view(request):
    yvu = CollegeDate.objects.filter(college='YOGI VEMUNA UNIVERSITY')
    context = {
        'yvu':yvu
    }
    return render(request,'COLLEGE/yvu.html',context)

def svu_view(request):
    svu = CollegeDate.objects.filter(college='SVU')
    context = {
        'svu':svu
    }
    return render(request,'COLLEGE/svu.html',context)

def mhu_view(request):
    mhu = CollegeDate.objects.filter(college='MAHARSTA UNIVERSITY')
    context = {
        'mhu':mhu
    }
    return render(request,'COLLEGE/mhu.html',context)

def du_view(request):
    du = CollegeDate.objects.filter(college='DELHI UNIVERSITY')
    context = {
        'du':du
    }
    return render(request,'COLLEGE/du.html',context)












