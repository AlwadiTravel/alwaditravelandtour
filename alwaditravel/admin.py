from django.contrib import admin
from django.urls import reverse

from .models import *
from django.utils.html import format_html


# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'FullName', 'other_name', 'passport_number', 'passport_copy', 'invitation_letter', 'apt_date',
                    'queue_number']
    list_filter = ['apt_date']
    search_fields = ['id', 'passport_number', 'first_name', 'second_name', 'last_name', 'apt_date']


admin.site.register(AppointmentSetting)
admin.site.register(Holidays)
