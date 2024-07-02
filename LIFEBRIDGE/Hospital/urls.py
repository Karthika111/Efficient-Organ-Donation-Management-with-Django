from django.urls import path,include
from Hospital import views
app_name='Hospital'
urlpatterns = [
    path('home/',views.home,name="Home"),
    path('myprofile/',views.Myprofile,name="MyProfile"),
    path('editprofile/',views.Editprofile,name="EditProfile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('Donor/',views.Donor,name="Donor"),
    path('Nominee/<int:did>',views.Nominee,name='Nominee'),
    path('Organ/<int:did>',views.Organ,name='Organ'),
    path('Accept/<int:did>',views.Accept,name='Accept'),
    path('Reject/<int:did>',views.Reject,name='Reject'),
    path("Complaint/",views.Complaint,name="Complaint"),
    path("Delcomplaint/<int:did>", views.Delcomplaint,name="Delcomplaint"),
    path("Feedback/",views.Feedback,name="Feedback"),
    path("Delfeedback/<int:did>", views.Delfeedback,name="Delfeedback"),
    path("logout/",views. logout,name="logout"),
]
