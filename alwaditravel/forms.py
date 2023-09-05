
from django import forms
from .models import *


class AppointmentMakeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppointmentMakeForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control'
            if f == 'apt_date':
                self.fields[f].widget.attrs['autocomplete'] = 'off'


    class Meta:
        model = Appointment
        fields = "__all__"
        widgets = {
            'queue_number': forms.HiddenInput(),

        }


class AppointmentDetailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppointmentDetailForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Appointment
        fields = "__all__"
