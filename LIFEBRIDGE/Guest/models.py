from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=20)
    user_email=models.CharField(max_length=20)
    user_contact=models.CharField(max_length=20)
    user_address=models.CharField(max_length=20)
    user_district=models.CharField(max_length=20)
    user_place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    user_photo=models.FileField(upload_to='user/')
    user_proof=models.FileField(upload_to='user/')
    user_password=models.CharField(max_length=20)

class tbl_hospital(models.Model):
    hospital_name=models.CharField(max_length=20)
    hospital_email=models.CharField(max_length=20)
    hospital_contact=models.CharField(max_length=20)
    hospital_address=models.CharField(max_length=20)
    hospital_district=models.CharField(max_length=20)
    hospital_place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    hospital_logo=models.FileField(upload_to='hospital/')
    hospital_proof=models.FileField(upload_to='hospital/')
    hospital_password=models.CharField(max_length=20)

