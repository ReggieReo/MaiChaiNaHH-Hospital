from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.base import View
from db.models import *
from db.filters import *
from db.forms import *


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
        context["create_form"] = PatientForm()
        return context


class PrescriptionMedicineView(ListView):
    queryset = PrescriptionMedicine.objects.all()
    template_name = "db/medicine.html"
    context_object_name = "medicines"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = MedicineFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        context["create_form"] = CreateMedicineForm()
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
        context["create_form"] = AppointmentForm()
        context["create_form"].fields['staff'].queryset = Staff.objects.filter(role__name="Doctor")
        return context


class AccountingView(ListView):
    queryset = Accounting.objects.all().order_by("-date")
    template_name = "db/accounting.html"
    context_object_name = "accountings"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AccountingFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        context["formsum"] = BalanceSumForm()
        context["create_form"] = AccountingForm()
        context["create_form"].fields['patient'].required = False
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
        context["create_form"] = DiseaseForm
        return context


class PrescriptionView(ListView):
    queryset = Prescription.objects.all()
    template_name = "db/prescription.html"
    context_object_name = "prescriptions"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PrescriptionFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        return context


class StaffView(ListView):
    queryset = Staff.objects.all()
    template_name = "db/staff.html"
    context_object_name = "staffs"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = StaffFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        context["create_form"] = StaffForm()
        return context


def balance_sum_by_date_range(request):
    if request.method == 'POST':
        form = BalanceSumForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # Query the database to get the sum of balances within the date range
            queryset = Accounting.objects.filter(date__range=(start_date, end_date))
            balance_sum = queryset.aggregate(Sum('balance'))['balance__sum']
            print(balance_sum)

            context = {
                'balance_sum': balance_sum,
                'queryset': queryset,
            }

            return render(request, 'db/balance_sum_result.html', context)


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
        context["create_form"] = CreateMedicineForm()
        return context


class EditMedicine(View):

    def get(self, request, pk):
        medicine = Medicine.objects.get(pk=pk)
        edit_form = MedicineEditForm(instance=medicine)
        context = {"medicine": medicine, "form": edit_form}
        return render(request, "db/edit_medicine.html", context)

    def post(self, request, pk):
        form = MedicineEditForm(request.POST, instance=Medicine.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            return redirect('db:medicine')


class DeleteMedicine(View):
    def get(self, requtest, pk):
        Medicine.objects.get(pk=pk).delete()
        redirect("db:medicine")


def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            diseases = form.cleaned_data['diseases']
            patient = form.save(commit=False)
            patient.save()
            for disease in diseases:
                patient.disease_set.add(disease)
            return redirect('db:index')


def create_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('db:staff')


class CreateMedicine(View):

    def post(self, request):
        form = CreateMedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('db:medicine')


class CreateDisease(View):

    def post(self, request):
        form = DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('db:disease')


class CreateAppointment(View):

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('db:appointment')


class CreateAccounting(View):

    def post(self, request):
        form = AccountingForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.hospital = Hospital.objects.get(id=1)
            account.save()
            return redirect('db:accounting')
        else:
            pat = form.cleaned_data.get("patient")
            expen = form.cleaned_data.get("is_expense")
            balance = form.cleaned_data.get("balance")
            date = form.cleaned_data.get("date")
            if pat is None and expen is True and balance < 0:
                account = Accounting(patient=None, balance=balance, date=date)
                account.hospital = Hospital.objects.get(id=1)
                account.save()
                print(account)
            return redirect('db:accounting')


class DeletePatient(View):

    def get(self, request, pk):
        patient = Patient.objects.get(pk=pk).delete()
        return redirect('db:index')


class EditPatient(View):

    def get(self, request, pk):
        patient = Patient.objects.get(pk=pk)
        edit_form = PatientForm(instance=patient)
        context = {"patient": patient, "form": edit_form}
        return render(request, "db/patient_edit.html", context)

    def post(self, request, pk):
        form = PatientForm(request.POST, instance=Patient.objects.get(pk=pk))
        if form.is_valid():
            diseases = form.cleaned_data['diseases']
            patient = form.save(commit=False)
            patient.save()
            for disease in diseases:
                patient.disease_set.add(disease)
            return redirect('db:index')


class DeleteStaff(View):

    def get(self, request, pk):
        staff = Staff.objects.get(pk=pk).delete()
        return redirect("db:staff")


class EditStaff(View):

    def get(self, request, pk):
        staff = Staff.objects.get(pk=pk)
        edit_form = StaffForm(instance=staff)
        context = {"staff": staff, "form": edit_form}
        return render(request, "db/staff_edit.html", context)

    def post(self, request, pk):
        form = StaffForm(request.POST, instance=Staff.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            return redirect('db:staff')


class DeleteDisease(View):
    def get(self, request, pk):
        Disease.objects.get(pk=pk).delete()
        return redirect("db:disease")


class EditDisease(View):

    def get(self, request, pk):
        disease = Disease.objects.get(pk=pk)
        edit_form = DiseaseForm(instance=disease)
        context = {"disease": disease, "form": edit_form}
        return render(request, "db/disease_edit.html", context)

    def post(self, request, pk):
        form = DiseaseForm(request.POST, instance=Disease.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            return redirect('db:disease')

        print("Not Pass")