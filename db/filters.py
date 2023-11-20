from django import forms
import django_filters
from db.models import *
from django_flatpickr.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput


class PatientFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="Patient's Name", widget=forms.TextInput(
        attrs={"class": "input input-bordered w-full max-w-xs mx-auto my-4 input-sm"}))
    staff__name = django_filters.CharFilter(lookup_expr="icontains", label="Doctor Name", widget=forms.TextInput(
        attrs={"class": "input input-bordered w-full max-w-xs mx-auto my-4 input-sm"}))
    room__room_number = django_filters.NumberFilter(label="Room")
    disease = django_filters.ModelChoiceFilter(queryset=Disease.objects.all(), label="Disease")

    def __init__(self, *args, **kwargs):
        super(PatientFilter, self).__init__(*args, **kwargs)
        self.filters['room__room_number'].field.widget = forms.Select(choices=self.get_room_choices())

    def get_room_choices(self):
        ROOM_CHOICES = {x.room_number: x.room_number for x in Room.objects.all()}
        ROOM_CHOICES[''] = "any"
        list_ = [(k, v) for k, v in ROOM_CHOICES.items()]
        list_ = tuple(list_)
        return list_

    class Meta:
        model = Patient
        fields = ["name", "staff__name", "room__room_number", "department", "disease"]


class MedicineFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="Medicine Name", widget=forms.TextInput(
        attrs={"class": "input input-bordered w-full max-w-xs mx-auto my-4 input-sm"}))
    prescriptionmedicine__prescription__staff__department__name = django_filters.ModelChoiceFilter(
        queryset=Department.objects.all(), label="Department")

    class Meta:
        model = Medicine
        fields = ["name", "prescriptionmedicine__prescription__staff__department__name"]


class AppointmentFilter(django_filters.FilterSet):
    staff = django_filters.ModelChoiceFilter(queryset=Staff.objects.filter(role__name="Doctor"))
    patient = django_filters.ModelChoiceFilter(queryset=Patient.objects.filter(appointment__isnull=False))
    dateTime = django_filters.DateTimeFilter(widget=DateTimePickerInput(
        attrs={'type': 'date', 'class': 'input input-bordered w-full max-w-xs mx-auto my-4 input-sm'}),
        lookup_expr="date")

    class Meta:
        model = Appointment
        fields = ["staff", "patient", "dateTime"]


class AccountingFilter(django_filters.FilterSet):
    balance = django_filters.NumberFilter(field_name="balance", label="Balance",
                                          widget=forms.TextInput(
                                              attrs={
                                                  "class": "input input-bordered w-full max-w-xs mx-auto my-4 input-sm"}))
    hospital = django_filters.ModelChoiceFilter(queryset=Hospital.objects.all(), label="Hospital")
    patient__name = django_filters.CharFilter(lookup_expr="icontains", label="Patient's Name", widget=forms.TextInput(
        attrs={"class": "input input-bordered w-full max-w-xs mx-auto my-4 input-sm"}))
    date = django_filters.DateTimeFromToRangeFilter(lookup_expr="date", widget=django_filters.widgets.RangeWidget(
        attrs={'type': 'date', 'class': 'input input-bordered w-full max-w-xs mx-auto my-4 input-sm'}))

    class Meta:
        model = Accounting
        fields = ["balance", "date", "hospital", "patient__name"]


class DiseaseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="Disease Name", widget=forms.TextInput(
        attrs={"class": "input input-bordered w-full max-w-xs mx-auto input-sm"}))
    patient__name = django_filters.CharFilter(lookup_expr="icontains", label="Patient Name", widget=forms.TextInput(
        attrs={"class": "input input-bordered w-full max-w-xs mx-auto input-sm"}))

    class Meta:
        model = Disease
        fields = ["name", "patient__name"]


class PrescriptionFilter(django_filters.FilterSet):
    staff = django_filters.ModelChoiceFilter(queryset=Staff.objects.filter(prescription__isnull=False).distinct())
    patient = django_filters.ModelChoiceFilter(queryset=Patient.objects.filter(prescription__isnull=False))
    prescriptionmedicine__medicine__name = django_filters.CharFilter(lookup_expr="icontains", label="Medicine Name")

    class Meta:
        model = Prescription
        fields = ["staff", "patient", "prescriptionmedicine__medicine__name"]


class StaffFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="Name")

    class Meta:
        model = Staff
        fields = ["name", "role", "department"]
