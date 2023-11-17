from django import forms
import django_filters
from db.models import *
from django_flatpickr.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput


# widget = forms.TextInput(attrs={"class": "input input-bordered w-full max-w-xs mx-auto my-4 input-sm"}),


def get_room_choice():
    ROOM_CHOICES = {x.room_number: x.room_number for x in Room.objects.all()}
    ROOM_CHOICES[''] = "any"
    list_ = [(k, v) for k, v in ROOM_CHOICES.items()]
    list_ = tuple(list_)
    return list_


class PatientFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="Patient's Name", widget=forms.TextInput(
        attrs={"class": "input input-bordered w-full max-w-xs mx-auto my-4 input-sm"}))
    staff__name = django_filters.CharFilter(lookup_expr="icontains", label="Doctor Name", widget=forms.TextInput(
        attrs={"class": "input input-bordered w-full max-w-xs mx-auto my-4 input-sm"}))
    room__room_number = django_filters.NumberFilter(widget=forms.Select(choices=get_room_choice()), label="Room")
    disease = django_filters.ModelChoiceFilter(queryset=Disease.objects.all(), label="Disease")

    class Meta:
        model = Patient
        fields = ["name", "staff__name", "room__room_number", "department", "disease"]


class PrescriptionMedicineFilter(django_filters.FilterSet):
    medicine__name = django_filters.CharFilter(lookup_expr="icontains", label="Medicine Name", widget=forms.TextInput(
        attrs={"class": "input input-bordered w-full max-w-xs mx-auto my-4 input-sm"}))
    prescription__staff__department__name = django_filters.ModelChoiceFilter(queryset=Department.objects.all())

    class Meta:
        model = Medicine
        fields = ["medicine__name", "prescription__staff__department__name"]


class AppointmentFilter(django_filters.FilterSet):
    staff = django_filters.ModelChoiceFilter(queryset=Staff.objects.filter(role__name="Doctor"))
    patient = django_filters.ModelChoiceFilter(queryset=Patient.objects.filter(appointment__isnull=False))
    dateTime = django_filters.DateTimeFilter(widget=DatePickerInput(), lookup_expr="date")

    class Meta:
        model = Appointment
        fields = ["staff", "patient", "dateTime"]


class AccountingFilter(django_filters.FilterSet):
    balance = django_filters.NumberFilter(field_name="balance", label="Balance",
                                          widget=forms.TextInput(
                                              attrs={"class": "input input-bordered w-full max-w-xs mx-auto my-4 input-sm"}))
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
