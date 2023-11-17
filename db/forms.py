from django import forms
from db.models import *


class BalanceSumForm(forms.Form):
    start_date = forms.DateTimeField(label='Start Date', widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateTimeField(label='End Date', widget=forms.TextInput(attrs={'type': 'date'}))


class PatientForm(forms.ModelForm):
    diseases = forms.ModelMultipleChoiceField(
        queryset=Disease.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    class Meta:
        model = Patient
        fields = ['name', 'address', 'phone_number', 'department', 'staff', 'age']


