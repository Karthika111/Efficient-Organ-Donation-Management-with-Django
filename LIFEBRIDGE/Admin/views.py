from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
from Hospital.models import *
from Guest.models import *
# Create your views here.
def district(request):
    district_data=tbl_district.objects.all()
    if request.method == 'POST':
        tbl_district.objects.create(district_name=request.POST.get("ddl_district"))
        return redirect("Wadmin:District")
    else:
        return render(request,"Admin/District.html",{'dis':district_data})
    

def DelDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Wadmin:District")


def EditDistrict(request,eid):
    district_data=tbl_district.objects.all()
    district=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        district.district_name=request.POST.get("ddl_district")
        district.save()
        return redirect("Wadmin:District")
    else:
        return render(request,"Admin/District.html",{'dis_data':district,'dis':district_data})


def place(request):
    place_data=tbl_place.objects.all()
    district_data=tbl_district.objects.all()
    if request.method=="POST":
        disid=tbl_district.objects.get(id=request.POST.get("ddl_district"))
        tbl_place.objects.create(
            place_name=request.POST.get("ddl_place"),
            
            district=disid
        )
        return render(request,"Admin/Place.html",{'place':place_data,'district':district_data})
    else:
        return render(request,"Admin/Place.html",{'place':place_data,'district':district_data})
    
def EditPlace(request,eid):
    plc=tbl_place.objects.get(id=eid)
    place_data=tbl_place.objects.all()
    district_data=tbl_district.objects.all()
    if request.method == "POST":
        district=tbl_district.objects.get(id=request.POST.get('ddl_district'))
        plc.district=district

        plc.place_name=request.POST.get("ddl_place")
       
        plc.save()
        return redirect("Wadmin:Place")
    else:
        return render(request,"Admin/Place.html",{'plc':plc,'place':place_data,'district':district_data})
    
def DelPlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("Wadmin:Place")

def organ(request):
    organ_data=tbl_organ.objects.all()
    if request.method == 'POST':
        tbl_organ.objects.create(organ_name=request.POST.get("txt_organ"))
        return redirect("Wadmin:Organs")
    else:
        return render(request,"Admin/Organs.html",{'org':organ_data})
    

def DelOrgan(request,did):
    tbl_organ.objects.get(id=did).delete()
    return redirect("Wadmin:Organs")


def EditOrgan(request,eid):
    organ_data=tbl_organ.objects.all()
    organ=tbl_organ.objects.get(id=eid)
    if request.method=="POST":
        organ.organ_name=request.POST.get("txt_organ")
        organ.save()
        return redirect("Wadmin:Organs")
    else:
       return render(request,"Admin/Organs.html",{'org_data':organ,'org':organ_data})

def bloodgroup(request):
    bloodgroup_data=tbl_bloodgroup.objects.all()
    if request.method == 'POST':
        tbl_bloodgroup.objects.create(bloodgroup_name=request.POST.get("txt_bloodgroup"))
        return redirect("Wadmin:Bloodgroup")
    else:
        return render(request,"Admin/Bloodgroup.html",{'bloodgroup':bloodgroup_data})
    

def DelBloodgroup(request,did):
    tbl_bloodgroup.objects.get(id=did).delete()
    return redirect("Wadmin:Bloodgroup")


def EditBloodgroup(request,eid):
    bloodgroup_data=tbl_bloodgroup.objects.all()
    bloodgroup=tbl_bloodgroup.objects.get(id=eid)
    if request.method=="POST":
        bloodgroup.bloodgroup_name=request.POST.get("txt_bloodgroup")
        bloodgroup.save()
        return redirect("Wadmin:Bloodgroup")
    else:
       return render(request,"Admin/Bloodgroup.html",{'bloodgroup_data':bloodgroup,'bloodgroup':bloodgroup_data})

def adminInsertSelect(request):
    adminData=tbl_admin.objects.all()
    if request.method == 'POST':
        tbl_admin.objects.create(admin_name=request.POST.get("txtname"),admin_email=request.POST.get("txtemail"),admin_contact=request.POST.get("txtcontact"),admin_password=request.POST.get("txtpassword"))
        return redirect("Wadmin:adminInsertSelect")
    else:
        return render(request,"Admin/AdminRegistration.html",{'adminData':adminData})
    

def deleteAdmin(request,did):
    tbl_admin.objects.get(id=did).delete()
    return redirect("Wadmin:adminInsertSelect")


def UpdateAdmin(request,eid):
    adminData=tbl_admin.objects.all()
    editdata=tbl_admin.objects.get(id=eid)
    if request.method=="POST":
        editdata.admin_name=request.POST.get("txtname")
        editdata.admin_email=request.POST.get("txtemail")
        editdata.admin_contact=request.POST.get("txtcontact")
        editdata.admin_password=request.POST.get("txtpassword")
        editdata.save()
        return redirect("Wadmin:adminInsertSelect")
    else:
        return render(request,"Admin/AdminRegistration.html",{'adminData':adminData,'editdata':editdata})


def home(request):
    if 'adminid' in request.session:
        name=request.session["adminname"]
        return render(request,"Admin/Home.html",{"name":name})
    else:
        return redirect('Guest:login')
    
def notification(request):
    notifData=tbl_notification.objects.all()
    if request.method == 'POST':
        tbl_notification.objects.create(notif_title=request.POST.get("txttitle"),notif_details=request.POST.get("txtnotification"))
        return redirect("Wadmin:notification")
    else:
        return render(request,"Admin/Notification.html",{'notifData':notifData})
    

def deleteNotification(request,did):
    tbl_notification.objects.get(id=did).delete()
    return redirect("Wadmin:notification")


def UpdateNotification(request,eid):
    notifData=tbl_notification.objects.all()
    editdata=tbl_notification.objects.get(id=eid)
    if request.method=="POST":
        editdata.notif_title_name=request.POST.get("txttitle")
        editdata.notif_details=request.POST.get("txtnotification")
        editdata.save()
        return redirect("Wadmin:notification")
    else:
        return render(request,"Admin/Notification.html",{'notifData':notifData,'editdata':editdata})

def Donor(request):
    data=tbl_donateform.objects.filter(donateform_status__gte=1)
    return render(request,'Admin/Donors.html',{'data':data})

def Nominee(request,did):
    donorid=tbl_donateform.objects.get(id=did)
    data=tbl_nominee.objects.filter(donor=donorid)
    return render(request,'Admin/ViewNominee.html',{'data':data})

def Organ(request,did):
    donorid=tbl_donateform.objects.get(id=did)
    data=tbl_donatingorgan.objects.filter(donor=donorid)
    return render(request,'Admin/ViewOrgans.html',{'data':data})

def DeathConfirmation(request):
    data=tbl_deathcase.objects.all()
    return render(request,'Admin/DeathConfirmation.html',{'data':data})

def Accept(request,did):
    data=tbl_deathcase.objects.get(id=did)
    data.case_status=1
    data.save()
    return redirect("Wadmin:DeathConfirmation")

def Reject(request,did):
    data=tbl_deathcase.objects.get(id=did)
    data.case_status=2
    data.save()
    return redirect("Wadmin:DeathConfirmation")

def ViewComplaint(request):
    newcom=tbl_complaint.objects.filter(complaint_status=0)
    recom=tbl_complaint.objects.filter(complaint_status=1)
    return render(request,"Admin/ViewComplaint.html",{'new':newcom,'repl':recom})  
def Reply(request,rid):
    com=tbl_complaint.objects.get(id=rid)
    if request.method=="POST":
        com.complaint_reply=request.POST.get("txtpro")
        com.complaint_status=1
        com.save()
        return redirect("Wadmin:ViewComplaint")
    else:
        return render(request,"Admin/Reply.html")
def ViewFeedback(request):
    data=tbl_feedback.objects.all()
    return render(request,"Admin/ViewFeedback.html",{'data':data})     

def Patient(request):
    data=tbl_patient.objects.all()
    return render(request,"Admin/ViewPatient.html",{'data':data})

def logout(request):
    if 'adminid' in request.session:
        del request.session['adminid']
        return redirect('Guest:index')
    else:
        return redirect('Guest:index')                   