from django import forms
import django_filters
from db.models import Patient, Room, Disease

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
