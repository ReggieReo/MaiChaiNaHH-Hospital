import django_filters
from django import forms
from db.models import *
from django_flatpickr.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput


class BalanceSumForm(forms.Form):
    start_date = forms.DateTimeField(label='Start Date', widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateTimeField(label='End Date', widget=forms.TextInput(attrs={'type': 'date'}))


class PatientForm(forms.ModelForm):
    diseases = forms.ModelMultipleChoiceField(
        queryset=Disease.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "input input-bordered w-full max-w-xs mx-auto my-4 input-sm"}))

    class Meta:
        model = Patient
        fields = ['name', 'address', 'phone_number', 'department', 'staff', 'age', 'diseases']


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ["name", "role", "department"]
        labels = {
            'name': "Name"
        }


class CreateMedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ["name", "amount", "price"]


class MedicineEditForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ["amount", "price"]


class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ["name"]


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["staff", "patient", "detail", "dateTime"]
        widgets = {
            'dateTime': DateTimePickerInput,
        }


class AccountingForm(forms.ModelForm):
    is_expense = forms.BooleanField(required=False)

    class Meta:
        model = Accounting
        fields = ["patient", "balance", "date"]
        widgets = {
            'date': DateTimePickerInput,
        }

    def clean(self):
        cleaned_data = super().clean()  # Call parent's clean method
        balance = cleaned_data.get("balance")
        is_expense = cleaned_data.get("is_expense")
        pat = cleaned_data.get("patient")

        if is_expense:
            if balance > 0 or pat is not None:
                print("Nope")
                raise forms.ValidationError("Nope")
        else:
            if balance < 0 or pat is None:
                print("Nope")
                raise forms.ValidationError("Nope")

        print("pass")

        return cleaned_data
