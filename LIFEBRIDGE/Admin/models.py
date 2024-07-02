from django.db import models

# Create your models here.
class tbl_district(models.Model):
   district_name=models.CharField(max_length=20)

class tbl_place(models.Model):
   place_name=models.CharField(max_length=20)
   district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_organ(models.Model):
   organ_name=models.CharField(max_length=20)

class tbl_bloodgroup(models.Model):
   bloodgroup_name=models.CharField(max_length=20)

class tbl_admin(models.Model):
   admin_name=models.CharField(max_length=20)
   admin_email=models.CharField(max_length=20)
   admin_contact=models.CharField(max_length=20)
   admin_password=models.CharField(max_length=20)

class tbl_notification(models.Model):
   notif_title=models.CharField(max_length=20)
   notif_details=models.CharField(max_length=20)