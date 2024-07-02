from django.urls import path,include
from User import views

app_name='User'

urlpatterns = [
    path('home/',views.home,name="Home"),
    path('myprofile/',views.Myprofile,name="MyProfile"),
    path('editprofile/',views.Editprofile,name="EditProfile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('donateform/',views.Donateform,name="donateform"),
    path("donatingorgans/<int:did>",views.organs,name="DonatingOrgans"),
    path("DelOrgan/<int:did>",views.DelOrgan,name="DelOrgan"),
    path("nominee/<int:did>",views.nominee,name="Nominee"),
    path("DelNominee/<int:did>",views.DelNominee,name="DelNominee"),
    path("patient/",views.patient,name="Patient"),
    path("DelPatient/<int:did>",views.DelPatient,name="DelPatient"),
    path("ViewDonors/",views.ViewDonors,name="ViewDonors"),
    path("DonationRequest/<int:did>",views.DonationRequest,name="DonationRequest"),
    path("ViewPateintRequest/",views.ViewPateintRequest,name="ViewPateintRequest"),

    path("Accept/<int:did>",views.Accept,name="Accept"),
    path("Reject/<int:did>",views.Reject,name="Reject"),

    path("ViewDonorRequest/",views.ViewDonorRequest,name="ViewDonorRequest"),

    path("Death/<int:did>",views.Death,name="Death"),

    path("DeleteDeath/<int:did>",views.DeleteDeath,name="DeleteDeath"),

    path("Complaint/",views.Complaint,name="Complaint"),
    path("Delcomplaint/<int:did>", views.Delcomplaint,name="Delcomplaint"),
    path("Feedback/",views.Feedback,name="Feedback"),
    path("Delfeedback/<int:did>", views.Delfeedback,name="Delfeedback"),


    path("logout/",views.logout,name="logout"),

]
