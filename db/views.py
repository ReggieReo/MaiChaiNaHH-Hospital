from django.shortcuts import render
from django.views.generic.list import ListView
from db.models import Patient, Medicine, Appointment
from db.models import Patient, Medicine, Accounting, Appointment
from db.filters import PatientFilter, MedicineFilter, AccountingFilter, AppointmentFilter


# Create your views here.


class PatientView(ListView):
    queryset = Patient.objects.all()
    template_name = "db/patient.html"
    context_object_name = "patients"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PatientFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context


class MedicineView(ListView):
    queryset = Medicine.objects.all()
    template_name = "db/medicine.html"
    context_object_name = "medicines"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = MedicineFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context


class AppointmentView(ListView):
    queryset = Appointment.objects.all()
    template_name = "db/appointment.html"
    context_object_name = "appointments"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AppointmentFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        return context


class AccountingView(ListView):
    queryset = Accounting.objects.all()
    template_name = "db/accounting.html"
    context_object_name = "accountings"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AccountingFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        return context
