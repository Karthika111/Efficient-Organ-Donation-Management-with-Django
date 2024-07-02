from django.urls import path,include
from Guest import views

app_name='Guest'

urlpatterns = [
    
    path("User/",views.user,name="user"),
    path('ajaxplace/',views.ajaxplace,name="ajaxplace"),
    path("HospitalRegistration/",views.hospital,name="HospitalRegistration"),
    path("Login/",views.login,name="Login"),
    path("",views.index,name="index"),
]