
from django import forms
from .models import *


class AppointmentMakeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppointmentMakeForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control'
            if f == 'apt_date':
                self.fields[f].widget.attrs['autocomplete'] = 'off'

    # def clean_files(self):
    #     data = self.cleaned_data['passport_copy', 'invitation_letter']
    #     print(data)
    #     if data[1] and data[2]:
    #         if data1.size > 0.25*1024*1024 or data1.size > 0.25*1024*1024:
    #             raise forms.ValidationError("File Size too large ( > 256kb ), must be less than 256kb")
    #         return data
    #     else:
    #         raise forms.ValidationError("Couldn't read uploaded image")
    

    # def clean_field(self):
    #     print('it is working')
    #     image = self.cleaned_data.get('passport_copy', False)
    #     if image:
    #         if image.size > 0.25*1024*1024:
    #             raise ValidationError("Image file too large ( > 256kb )")
    #         return image
    #     else:
    #         raise ValidationError("Couldn't read uploaded image")

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
