from datetime import datetime
from django.core.exceptions import ValidationError

from django.db import models

def validate_file_size(value):
    filesize= value.size
    
    if filesize > 262144:
        raise ValidationError("The maximum file size that can be uploaded is 256kb")
    else:
        return value
# Create your models here.
class Appointment(models.Model):
    first_name = models.CharField(max_length=30, blank=False, null=False)
    second_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    other_name = models.CharField(max_length=30, blank=False, null=False)
    passport_number = models.CharField(max_length=30, blank=False, null=False)
    passport_copy = models.ImageField(upload_to='uploads', validators=[validate_file_size])
    invitation_letter = models.FileField(upload_to='uploads',validators=[validate_file_size])
    apt_date = models.DateField(verbose_name="Appointment Date")
    queue_number = models.IntegerField(default=-1)

    def FullName(self):
        return str(self.first_name + " " + self.second_name + " " + self.last_name)

    def __str__(self):
        """String for representing the Model object."""
        return str(self.first_name + " " + self.second_name)


class AppointmentSetting(models.Model):
    apt_date = models.DateField()
    apt_limit = models.IntegerField(blank=False, null=False, default=50)

    def __str__(self):
        """String for representing the Model object."""
        return str(self.apt_date)


class Holidays(models.Model):
    name = models.CharField(max_length=60)
    h_date = models.DateField()

    def chech_holiday(self):
        AppointmentSetting.objects.filter(apt_date=self.h_date).update(apt_status=False)
