from django.urls import path

from db.views import PatientView, MedicineView

app_name = "db"
urlpatterns = [
    path("", PatientView.as_view(), name="index"),
    path("medicine", MedicineView.as_view(), name="medicine")
]
