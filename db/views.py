from django.shortcuts import render
from django.views.generic.list import ListView
from db.models import *
from db.filters import *


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


class PrescriptionMedicineView(ListView):
    queryset = PrescriptionMedicine.objects.all()
    template_name = "db/medicine.html"
    context_object_name = "medicines"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PrescriptionMedicineFilter(self.request.GET, queryset)
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


class DiseaseView(ListView):
    queryset = Disease.objects.all()
    template_name = "db/disease.html"
    context_object_name = "diseases"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = DiseaseFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        return context
