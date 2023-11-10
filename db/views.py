from django.shortcuts import render
from django.views.generic.list import ListView
from db.models import Patient
from db.filters import PatientFilter


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
