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
    path("create_accounting", CreateAccounting.as_view(), name="create_accounting"),
    path("delete_patient/<int:pk>", DeletePatient.as_view(), name="delete_patient"),
    path("edit_patient/<int:pk>", EditPatient.as_view(), name="edit_patient"),
    path("delete_staff/<int:pk>", DeleteStaff.as_view(), name="delete_staff"),
    path("edit_staff/<int:pk>", EditStaff.as_view(), name="edit_staff"),
    path("delete_disease/<int:pk>", DeleteDisease.as_view(), name="delete_disease"),
    path("edit_disease/<int:pk>", EditDisease.as_view(), name="edit_disease"),
    path("delete_appointment/<int:pk>", DeleteAppointment.as_view(), name="delete_appointment"),
    path("edit_appointment/<int:pk>", EditAppointment.as_view(), name="edit_appointment"),
    path("delete_dedicine/<int:pk>", DeleteMedicine.as_view(), name="delete_medicine"),
]
