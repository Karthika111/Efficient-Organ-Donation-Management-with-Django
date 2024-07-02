from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from Hospital.models import *

# Create your views here.
def home(request):
    if 'hospitalid' in request.session:
        name=request.session["hospitalname"]
        return render(request,"Hospital/Home.html",{"name":name})
    else:
        return redirect('Guest:login')

def Myprofile(request):
    hospital_data=tbl_hospital.objects.get(id=request.session['hospitalid'])
    return render(request,"Hospital/MyProfile.html",{'hospital':hospital_data})

def Editprofile(request):
            hospital_data=tbl_hospital.objects.get(id=request.session['hospitalid'])
            if request.method=='POST':
                hospital_data.hospital_name=request.POST.get("txt_hospitalname")
                hospital_data.hospital_contact=request.POST.get("txt_hospitalcontact")
                hospital_data.hospital_address=request.POST.get("txt_hospitaladdress")
                hospital_data.save()
                return redirect('Hospital:MyProfile')
            else:
                return render(request,"Hospital/EditProfile.html",{'hospital':hospital_data})


def changepassword(request):
    if request.method=="POST":
        ccount=tbl_hospital.objects.filter(id=request.session["hospitalid"],hospital_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                hospitaldata=tbl_hospital.objects.get(id=request.session["hospitalid"],hospital_password=request.POST.get('txtcurpass'))
                hospitaldata.hospital_password=request.POST.get('txtnewpass')
                hospitaldata.save()
                return render(request,"Hospital/Changepassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Hospital/Changepassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Hospital/Changepassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Hospital/Changepassword.html")

def Donor(request):
    hospital_data=tbl_hospital.objects.get(id=request.session['hospitalid'])
    data=tbl_donateform.objects.filter(hospital=hospital_data)
    return render(request,'Hospital/DonorVerification.html',{'data':data})

def Nominee(request,did):
    donorid=tbl_donateform.objects.get(id=did)
    data=tbl_nominee.objects.filter(donor=donorid)
    return render(request,'Hospital/ViewNominee.html',{'data':data})

def Organ(request,did):
    donorid=tbl_donateform.objects.get(id=did)
    data=tbl_donatingorgan.objects.filter(donor=donorid)
    return render(request,'Hospital/ViewOrgans.html',{'data':data})

def Accept(request,did):
    data=tbl_donateform.objects.get(id=did)
    data.donateform_status=1
    data.save()
    return redirect("Hospital:Donor")

def Reject(request,did):
    data=tbl_donateform.objects.get(id=did)
    data.donateform_status=2
    data.save()
    return redirect("Hospital:Donor")


def Complaint(request):
    customerdata=tbl_hospital.objects.get(id=request.session["hospitalid"])
    Complaint=tbl_complaint.objects.filter(hospital=customerdata)
    if request.method=="POST":
       tbl_complaint.objects.create(hospital=customerdata,
                                    complaint_title=request.POST.get("txttit"),
                                    complaint_content=request.POST.get("txtcomplaint"))
       return redirect("Hospital:Complaint")
    else:
        return render(request,"Hospital/Complaint.html",{'complaint':Complaint}) 

def Delcomplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("Hospital:Complaint")

def Feedback(request):
    customerdata=tbl_hospital.objects.get(id=request.session["hospitalid"])
    feedback=tbl_feedback.objects.filter(hospital=customerdata)
    if request.method=="POST":
       tbl_feedback.objects.create(hospital=customerdata,
                                   feedback_content=request.POST.get("txtpro"))
       return redirect("Hospital:Feedback")
    else:
        return render(request,"Hospital/Feedback.html",{'feedback':feedback})       

def Delfeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect("Hospital:Feedback")   

def logout(request):
    if 'hospitalid' in request.session:
        del request.session['hospitalid']
        return redirect('Guest:index')
    else:
        return redirect('Guest:index')                   