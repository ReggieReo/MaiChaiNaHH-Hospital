from django.urls import path


from db.views import *


app_name = "db"
urlpatterns = [
    path("", PatientView.as_view(), name="index"),
    path("medicine", MedicineView.as_view(), name="medicine"),
    path("appointment", AppointmentView.as_view(), name="appointment"),
    path("accounting", AccountingView.as_view(), name="accounting"),
    path("disease", DiseaseView.as_view(), name="disease"),
    path("prescription", PrescriptionView.as_view(), name="prescription"),
    path("staff", StaffView.as_view(), name="staff"),
    path("sum", balance_sum_by_date_range, name="sum"),
    path("create_patient", create_patient, name="create_patient"),
    path("create_staff", create_staff, name="create_staff"),
    path("create_disease", CreateDisease.as_view(), name="create_disease"),
    path("edit_medicine/<int:pk>", EditMedicine.as_view(), name="edit_medicine"),
    path("create_medicine", CreateMedicine.as_view(), name="create_medicine"),
    path("create_appointment", CreateAppointment.as_view(), name="create_appointment"),
]
