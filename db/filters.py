from django import forms
import django_filters
from db.models import *


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


class MedicineFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="Medicine Name", widget=forms.TextInput(
        attrs={"class": "input input-bordered w-full max-w-xs mx-auto my-4 input-sm"}))
    department = django_filters.ModelChoiceFilter(queryset=Department.objects.all(), label="Department")

    class Meta:
        model = Medicine
        fields = ["name", "department"]


class AppointmentFilter(django_filters.FilterSet):
    staff = django_filters.ModelChoiceFilter(queryset=Staff.objects.filter(role__name="Doctor"))
    patient = django_filters.ModelChoiceFilter(queryset=Patient.objects.filter(appointment__isnull=False))
    dateTime = django_filters.DateTimeFilter()

    class Meta:
        model = Appointment
        fields = ["staff", "patient", "dateTime"]
