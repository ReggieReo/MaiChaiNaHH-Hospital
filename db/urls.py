from django.urls import path


from db.views import *


app_name = "db"
urlpatterns = [
    path("", PatientView.as_view(), name="index"),
    path("medicine", MedicineView.as_view(), name="medicine"),
    path("appointment", AppointmentView.as_view(), name="appointment"),
    path("accounting", AccountingView.as_view(), name="accounting"),
    path("disease", DiseaseView.as_view(), name="disease"),
]
