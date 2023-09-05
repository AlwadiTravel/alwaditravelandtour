from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('appointment/<pk>/detail', AppointmentDetail.as_view(), name='appointment-detail'),
    path('appointment/make', AppointmentMake.as_view(), name='appointment-make'),

]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

