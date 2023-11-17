from django import forms


class BalanceSumForm(forms.Form):
    start_date = forms.DateTimeField(label='Start Date', widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateTimeField(label='End Date', widget=forms.TextInput(attrs={'type': 'date'}))
