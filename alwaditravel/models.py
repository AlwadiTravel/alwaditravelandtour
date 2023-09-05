from datetime import datetime

from django.db import models


# Create your models here.
class Appointment(models.Model):
    first_name = models.CharField(max_length=30, blank=False, null=False)
    second_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    other_name = models.CharField(max_length=30, blank=False, null=False)
    passport_number = models.IntegerField(blank=False, null=False)
    passport_copy = models.ImageField(upload_to='uploads')
    invitation_letter = models.FileField(upload_to='uploads')
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
