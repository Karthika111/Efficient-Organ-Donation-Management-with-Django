from django.db import models
from Guest.models import tbl_hospital, tbl_user
from User.models import *
from Admin.models import *
# Create your models here.
class tbl_donateform(models.Model):
    donateform_gender=models.CharField(max_length=20)
    bloodgroup=models.ForeignKey(tbl_bloodgroup,on_delete=models.CASCADE)
    donateform_DOB=models.CharField(max_length=20)
    hospital=models.ForeignKey(tbl_hospital,on_delete=models.CASCADE)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    donateform_status=models.CharField(max_length=20,default=0)

class tbl_donatingorgan(models.Model):
    donor=models.ForeignKey(tbl_donateform,on_delete=models.CASCADE)
    organs=models.ForeignKey(tbl_organ,on_delete=models.CASCADE)
    donation_status=models.CharField(max_length=10,default=0)

class tbl_nominee(models.Model):
    nominee_name=models.CharField(max_length=20)
    nominee_relation=models.CharField(max_length=20)
    nominee_email=models.CharField(max_length=20)
    nominee_proof=models.FileField(upload_to='nominee/')
    donor=models.ForeignKey(tbl_donateform,on_delete=models.CASCADE,null=True)

class tbl_patient(models.Model):
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    patient_gender=models.CharField(max_length=20)
    patient_bloodgroup=models.ForeignKey(tbl_bloodgroup, on_delete=models.CASCADE,null=True)
    patient_DOB=models.CharField(max_length=20)
    patient_consultinghospital=models.CharField(max_length=20)
    organdata=models.ForeignKey(tbl_organ, on_delete=models.CASCADE,null=True)

class tbl_request(models.Model):
    patient=models.ForeignKey(tbl_patient,on_delete=models.CASCADE)
    donor=models.ForeignKey(tbl_donateform,on_delete=models.CASCADE)
    request_status=models.CharField(max_length=10,default=0)
    requested_date=models.DateField(auto_now_add=True)

class tbl_deathcase(models.Model):
    death_certificate=models.FileField(upload_to='CasesDocs/')
    donor=models.ForeignKey(tbl_donateform,on_delete=models.CASCADE)
    nominee_name=models.CharField(max_length=50)
    case_status=models.CharField(max_length=10,default=0)

class tbl_complaints(models.Model):
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    complaint_status=models.CharField(default=0,max_length=10)
    complaint_title=models.CharField(max_length=100)
    complaint_content=models.CharField(max_length=300)
    complaint_reply=models.CharField(default='Not replied',max_length=100)
    complaint_date=models.DateField(auto_now_add=True)

class tbl_feedbacks(models.Model):
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    feedback_content=models.CharField(max_length=300)
    feedback_date=models.DateField(auto_now_add=True)