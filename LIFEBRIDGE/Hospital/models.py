from django.db import models
from User.models import *
from Admin.models import *
from Guest.models import *
from Hospital.models import *

# Create your models here.
class tbl_complaint(models.Model):
    hospital=models.ForeignKey(tbl_hospital,on_delete=models.CASCADE)
    complaint_status=models.CharField(default=0,max_length=10)
    complaint_title=models.CharField(max_length=100)
    complaint_content=models.CharField(max_length=300)
    complaint_reply=models.CharField(default='Not replied',max_length=100)
    complaint_date=models.DateField(auto_now_add=True)

class tbl_feedback(models.Model):
    hospital=models.ForeignKey(tbl_hospital,on_delete=models.CASCADE)
    feedback_content=models.CharField(max_length=300)
    feedback_date=models.DateField(auto_now_add=True)