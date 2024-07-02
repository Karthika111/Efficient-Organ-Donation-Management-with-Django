from django.shortcuts import  render, redirect
from Guest.models import *
from User.models import *
from Admin.models import *
# Create your views here.

def user(request):
    dis=tbl_district.objects.all()
    user=tbl_user.objects.all()
    if request.method=="POST" and request.FILES:
        plcid=tbl_place.objects.get(id=request.POST.get("ddl_place"))
        tbl_user.objects.create(user_name=request.POST.get("txt_name"),
                               user_email=request.POST.get("txt_email"),
                               user_contact=request.POST.get("txt_contact"),
                               user_address=request.POST.get("txt_address"),
                               user_district=request.POST.get("ddl_district"),
                               user_place=plcid,
                               user_photo=request.FILES.get("file_photo"),
                               user_proof=request.FILES.get("file_proof"),
                               user_password=request.POST.get("txt_pass"),
                               )
        return render(request,"Guest/User.html",{"dis":dis})
    else:
        return render(request,"Guest/User.html",{"dis":dis})

def hospital(request):
    dis=tbl_district.objects.all()
    hospital=tbl_hospital.objects.all()
    if request.method=="POST":
        plcid=tbl_place.objects.get(id=request.POST.get('ddl_place'))
        tbl_hospital.objects.create(hospital_name=request.POST.get("txt_name"),
                               hospital_email=request.POST.get("txt_email"),
                               hospital_contact=request.POST.get("txt_contact"),
                               hospital_address=request.POST.get("txt_address"),
                               hospital_district=request.POST.get("ddl_district"),
                               hospital_place=plcid,
                               hospital_logo=request.FILES.get("file_logo"),
                               hospital_proof=request.FILES.get("file_proof"),
                               hospital_password=request.POST.get("txt_pass")),
                               


        return render(request,"Guest/HospitalRegistration.html",{"dis":dis})
    else:
        return render(request,"Guest/HospitalRegistration.html",{"dis":dis})

def ajaxplace(request):
    dist = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dist)
    return render(request,"Guest/AjaxPlace.html",{"place":place})

def login(request):
    if request.method=="POST":
        email = request.POST.get("txt_email")
        password = request.POST.get("txt_password")
        confirmpassword = request.POST.get("txt_repass")
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        hospitalcount=tbl_hospital.objects.filter(hospital_email=email,hospital_password=password).count()
        admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()

        if usercount>0:
            
            user=tbl_user.objects.get(user_email=email,user_password=password)
            request.session["userid"]=user.id
            request.session["username"]=user.user_name
            return redirect('User:Home')
        
        elif hospitalcount>0:
            hospital=tbl_hospital.objects.get(hospital_email=email,hospital_password=password)
            request.session["hospitalid"]=hospital.id
            request.session["hospitalname"]=hospital.hospital_name
            return redirect('Hospital:Home')
        
        elif admincount>0:
            admin=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session["adminid"]=admin.id
            request.session["adminname"]=admin.admin_name
            return redirect('Wadmin:Home')
     
     
        else:
            return render(request,"Guest/Login.html")
    else:
        return render(request,"Guest/Login.html")
    
def index(request):
    return render(request,"Guest/index.html")

