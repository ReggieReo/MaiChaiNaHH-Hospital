from django.urls import path

from db.views import PatientView

app_name = "db"
urlpatterns = [
    path("", PatientView.as_view(), name="index"),
]
