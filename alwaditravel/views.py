from django.contrib.messages.views import SuccessMessageMixin

from django.shortcuts import render
from django.http.response import HttpResponseRedirect, Http404

from django.views.generic import *
from .forms import *
from django.contrib import messages


def home(request, lng="ar"):
    return render(request, template_name='alwaditravel/index.html', context={"lng": lng, "current_url_name": "home"})


# checks if the view is refered from another view
def get_referer(request):
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return None
    return referer


class AppointmentMake(CreateView, SuccessMessageMixin):
    model = Appointment
    form_class = AppointmentMakeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        h = Holidays.objects.all().values('h_date')
        c = AppointmentSetting.objects.filter(apt_limit=0).values('apt_date')

        context['holidays'] = h
        context['apt_count'] = c
        a_form = ['الاسم الأول', 'اسم الأب', 'اسم الجد', 'اسم العائلة', 'رقم جواز السفر', 'صورة جواز السفر',
                             'مستند تأشيرة', 'تاريخ الموعد','']
        context['gg'] = zip(self.get_form(), a_form)
        return context

    def form_valid(self, form):

        # clean the data

        data = form.cleaned_data

        # check the existing AppointmentSetting object
        apt_Setting_exist = AppointmentSetting.objects.filter(apt_date=data.get("apt_date"))

        apt_setting_obj = None
        if (len(apt_Setting_exist) > 0):  # load appointment setting object
            apt_setting_obj = apt_Setting_exist[0]
        else:  # create new setting object
            apt_setting_obj = AppointmentSetting.objects.create(apt_date=data.get("apt_date"))

        booked_today = Appointment.objects.filter(passport_number=data.get("passport_number"),
                                                  apt_date=data.get("apt_date")).exists()

        if (booked_today):
            messages.error(self.request, message="You can not Book twice per day")

            return HttpResponseRedirect("/appointment/make")
        # maximum limit reached
        if (apt_setting_obj.apt_limit <= 0):
            messages.error(self.request, message="Appointment for the selected date is full")
            return HttpResponseRedirect("/appointment/make")

        # save form
        self.object = form.save()

        # update and save appontment setting object
        apt_setting_obj.apt_limit -= 1
        apt_setting_obj.save()

        # update the queue number
        self.object.queue_number = 50 - apt_setting_obj.apt_limit
        self.object.save()

        messages.success(self.request, "Your Appointment is Booked Successfully !")
        return HttpResponseRedirect('/appointment/' + str(self.object.id) + '/detail')


class AppointmentDetail(DetailView):
    model = Appointment
    form_class = AppointmentDetailForm

    def get(self, request, *args, **kwargs):
        if not get_referer(self.request):
            return HttpResponseRedirect('/')

        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        return self.render_to_response(context)
