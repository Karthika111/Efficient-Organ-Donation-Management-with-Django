from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from Hospital.models import *
from django.core.mail  import send_mail
# Create your views here.
def home(request):
    if 'userid' in request.session:
        name=request.session["username"]
        return render(request,"User/Home.html",{"name":name})
    else:
        return redirect('Guest:login')
    
def Myprofile(request):
    user_data=tbl_user.objects.get(id=request.session['userid'])
    return render(request,"User/MyProfile.html",{'user':user_data})

def Editprofile(request):
            user_data=tbl_user.objects.get(id=request.session['userid'])
            if request.method=='POST':
                user_data.user_name=request.POST.get("txt_username")
                user_data.user_contact=request.POST.get("txt_usercontact")
                user_data.user_address=request.POST.get("txt_useraddress")
                user_data.save()
                return redirect('User:MyProfile')
            else:
                return render(request,"User/EditProfile.html",{'user':user_data})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_user.objects.filter(id=request.session["userid"],user_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_user.objects.get(id=request.session["userid"],user_password=request.POST.get('txtcurpass'))
                userdata.user_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"User/Changepassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"User/Changepassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"User/Changepassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"User/Changepassword.html")

def Donateform(request):
   blood = tbl_bloodgroup.objects.all()
   user_data=tbl_user.objects.get(id=request.session['userid'])
   hos=tbl_hospital.objects.all()
   data=tbl_donateform.objects.filter(user=user_data)
   if request.method=="POST":
       selblood=tbl_bloodgroup.objects.get(id=request.POST.get("bloodgroup"))
       selhos=tbl_hospital.objects.get(id=request.POST.get("txt_hospital"))
       tbl_donateform.objects.create(donateform_gender=request.POST.get("rdo_gender"),
                                     bloodgroup=selblood,
                                     donateform_DOB=request.POST.get("txt_dob"),
                                     hospital=selhos,
                                     user=user_data)
       return render(request,"User/DonateForm.html",{'donateform':user_data,"bloodgroup":blood,'hos':hos,'data':data})
   else:
       return render(request,"User/DonateForm.html",{'donateform':user_data,"bloodgroup":blood,'hos':hos,'data':data})




def organs(request, did):
    organ = tbl_organ.objects.all()
    donorid = tbl_donateform.objects.get(id=did)
    organ_data = tbl_donatingorgan.objects.filter(donor=donorid)

    if request.method == 'POST':
        selected_organs = request.POST.getlist('selected_organs')
        for organ_id in selected_organs:
            organ_obj = tbl_organ.objects.get(id=organ_id)
            tbl_donatingorgan.objects.create(donor=donorid, organs=organ_obj, donation_status='0')
        return redirect("User:DonatingOrgans",did=did)  

    return render(request, "User/DonatingOrgans.html", {'org_data': organ, 'org': organ_data})

def DelOrgan(request,did):
    tbl_donatingorgan.objects.get(id=did).delete()
    return redirect("User:donateform")

def nominee(request,did):
    donorid = tbl_donateform.objects.get(id=did)

    dname=donorid.user.user_name
    demail=donorid.user.user_email
    dpass=donorid.user.user_password

    nominee_data=tbl_nominee.objects.filter(donor=donorid)
    if request.method == 'POST':
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        tbl_nominee.objects.create(nominee_name=request.POST.get("txt_name"),
        nominee_relation=request.POST.get("txt_relation"),
        nominee_email=request.POST.get("txt_email"),
        nominee_proof=request.FILES.get("file_proof"),
        donor=donorid)
        subject = 'Donation Registration'
        message = f'Dear {name},\n\nYou are selected as a nominee of {dname}.You can login using provided email and password.\n\n Email:{demail} \n\n Password:{dpass}\n\nThank You!!!'
        from_email = 'lifebridge4@gmail.com' 
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)
        return redirect("User:Nominee",did=did)
    else:
        return render(request,"User/Nominee.html",{'nominee':nominee_data})
    

def DelNominee(request,did):
    tbl_nominee.objects.get(id=did).delete()
    return redirect("User:donateform")


def patient(request):
    user_data=tbl_user.objects.get(id=request.session['userid'])
    patient_data=tbl_patient.objects.filter(user=user_data)
    blood = tbl_bloodgroup.objects.all()
    org = tbl_organ.objects.all()
    if request.method == 'POST':
        org_data = tbl_organ.objects.get(id=request.POST.get("neededorgan"))
        sel_blood = tbl_bloodgroup.objects.get(id=request.POST.get("txt_bloodgroup"))
        tbl_patient.objects.create(user=user_data,
        patient_gender=request.POST.get("rdo_gender"),
        patient_bloodgroup=sel_blood,
        patient_DOB=request.POST.get("txt_dob"),
        patient_consultinghospital=request.POST.get("txt_hospital"),
        organdata=org_data)
        return redirect("User:Patient")
    else:
        return render(request,"User/Patient.html",{'patient':patient_data,"bloodgroup":blood,"neededorgan":org,'user':user_data})
    

def DelPatient(request,did):
    tbl_patient.objects.get(id=did).delete()
    return redirect("User:Patient")

def ViewDonors(request):
    user_data=tbl_user.objects.get(id=request.session['userid'])
    pcount=tbl_patient.objects.filter(user=user_data).count()
    if pcount>0:
        patient_data=tbl_patient.objects.get(user=user_data)
        bgroup=patient_data.patient_bloodgroup.id
        org=patient_data.organdata.id
        data=tbl_donatingorgan.objects.filter(organs=org,donor__bloodgroup=bgroup,donor__donateform_status=1)
        # print(data)
        return render(request,"User/ViewDonors.html",{'donation_forms':data})
    else:
        return render(request,"User/ViewDonors.html")

def DonationRequest(request,did):
    user_data=tbl_user.objects.get(id=request.session['userid'])
    patient_data=tbl_patient.objects.get(user=user_data)
    donor_data=tbl_donateform.objects.get(id=did)
    demail=donor_data.user.user_email
    dname=donor_data.user.user_name
    ndata=tbl_nominee.objects.filter(donor=donor_data)
    
    for data in ndata :
        nemail=data.nominee_email
        subject = 'New Patient Request'
        message = f'\n\nDonor {dname} got a new request for organ from  a patient.Please login into the accout using provided email and password.\n\nThank You!!!'
        from_email = 'lifebridge4@gmail.com' 
        recipient_list = [nemail]

        send_mail(subject, message, from_email, recipient_list)
    subject = 'New Patient Request'
    message = f'\n\nDonor {dname} got a new request for organ from  a patient.Please login into the accout using provided email and password.\n\nThank You!!!'
    from_email = 'lifebridge4@gmail.com' 
    recipient_list = [demail]

    send_mail(subject, message, from_email, recipient_list)
    tbl_request.objects.create(patient=patient_data,donor=donor_data)
    return redirect("User:ViewDonors")

def ViewPateintRequest(request):
    user_data=tbl_user.objects.get(id=request.session['userid'])
    dcount=tbl_donateform.objects.filter(user=user_data,donateform_status=1).count()
    if dcount>0:
        donor_data=tbl_donateform.objects.get(user=user_data,donateform_status=1)
        rdata=tbl_request.objects.filter(donor=donor_data)
        return render(request,"User/ViewPatientRequest.html",{'data':rdata})
    else:
        return render(request,"User/ViewPatientRequest.html")
    
def Accept(request,did):
    data=tbl_request.objects.get(id=did)
    data.request_status=1
    data.save()
    return redirect("User:ViewPateintRequest")

def Reject(request,did):
    data=tbl_request.objects.get(id=did)
    data.request_status=2
    data.save()
    return redirect("User:ViewPateintRequest")

def ViewDonorRequest(request):
    user_data=tbl_user.objects.get(id=request.session['userid'])
    pcount=tbl_patient.objects.filter(user=user_data).count()
    if pcount>0:
        patient_data=tbl_patient.objects.get(user=user_data)
        rdata=tbl_request.objects.filter(patient=patient_data)
        return render(request,"User/ViewDonorRequest.html",{'data':rdata})
    else:
        return render(request,"User/ViewDonorRequest.html")
    
def Death(request,did):
    donor_data=tbl_donateform.objects.get(id=did)
    cdata=tbl_deathcase.objects.filter(donor=donor_data)
    if request.method=="POST":
        tbl_deathcase.objects.create(death_certificate=request.FILES.get("Certificate"),
                                     donor=donor_data,
                                     nominee_name=request.POST.get("cnominee"))
        return redirect("User:Death",did=did)

    else:
        return render(request,"User/DeathConfirmation.html",{'data':cdata})
    
def DeleteDeath(request,did):
    tbl_deathcase.objects.get(id=did).delete()
    return redirect("User:donateform")

def Complaint(request):
    customerdata = tbl_user.objects.get(id=request.session["userid"])
    user_complaints = tbl_complaints.objects.filter(user=customerdata)
    if request.method == "POST":
        tbl_complaints.objects.create(
            user=customerdata,
            complaint_title=request.POST.get("txttit"),
            complaint_content=request.POST.get("txtcomplaint")
        )
        return redirect("User:Complaint")
    else:
        return render(request, "User/Complaint.html", {'complaints': user_complaints})

def Delcomplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("User:Complaint")

def Feedback(request):
    customerdata=tbl_user.objects.get(id=request.session["userid"])
    feedback=tbl_feedbacks.objects.filter(user=customerdata)
    if request.method=="POST":
       tbl_feedbacks.objects.create(user=customerdata,
                                   feedback_content=request.POST.get("txtpro"))
       return redirect("User:Feedback")
    else:
        return render(request,"User/Feedback.html",{'feedback':feedback})       

def Delfeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect("User:Feedback")   

def logout(request):
    if 'userid' in request.session:
        del request.session['userid']
        return redirect('Guest:index')
    else:
        return redirect('Guest:index')       