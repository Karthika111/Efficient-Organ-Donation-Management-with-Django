from django.urls import path,include
from Admin import views
app_name='Wadmin'
urlpatterns = [
    path("district/",views.district,name="District"),
    path("place/",views.place,name="Place"),
    path("DelDistrict/<int:did>",views.DelDistrict,name="DelDistrict"),
    path("EditDistrict/<int:eid>",views.EditDistrict,name="EditDistrict"),
    path("DelPlace/<int:did>",views.DelPlace,name="DelPlace"),
    path("EditPlace/<int:eid>",views.EditPlace,name="EditPlace"),
    path("organ/",views.organ,name="Organs"),
    path("DelOrgan/<int:did>",views.DelOrgan,name="DelOrgan"),
    path("EditOrgan/<int:eid>",views.EditOrgan,name="EditOrgan"),
    path("bloodgroup/",views.bloodgroup,name="Bloodgroup"),
    path("DelBloodgroup/<int:did>",views.DelBloodgroup,name="DelBloodgroup"),
    path("EditBloodgroup/<int:eid>",views.EditBloodgroup,name="EditBloodgroup"),

    path("AdminRegistration/",views.adminInsertSelect,name="adminInsertSelect"),
    path("UpdateAdmin/<int:eid>",views.UpdateAdmin,name="UpdateAdmin"),
    path("deleteAdmin/<int:did>",views.deleteAdmin,name="deleteAdmin"),
    path('home/',views.home,name="Home"),
    

    path("Notification/",views.notification,name="notification"),
    path("UpdateNotification/<int:eid>",views.UpdateNotification,name="UpdateNotification"),
    path("deleteNotification/<int:did>",views.deleteNotification,name="deleteNotification"),

    path('Donor/',views.Donor,name="Donor"),
    path('Nominee/<int:did>',views.Nominee,name='Nominee'),
    path('Organ/<int:did>',views.Organ,name='Organ'),

    path('DeathConfirmation/',views.DeathConfirmation,name="DeathConfirmation"),
    path('Accept/<int:did>',views.Accept,name='Accept'),
    path('Reject/<int:did>',views.Reject,name='Reject'),

    path("ViewComplaint/",views. ViewComplaint,name="ViewComplaint"),
    path("Reply/<int:rid>",views. Reply,name="Reply"),
    path("ViewFeedback/",views. ViewFeedback,name="ViewFeedback"),

    path('Patient/',views.Patient,name="Patient"),

    path("logout/",views. logout,name="logout"),
]

