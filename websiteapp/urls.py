from django.urls import path
from .views import ListDevices, CreateDevice, DetailDevice, Integration, signup_view

app_name = 'websiteapp'

urlpatterns = [
    path('', ListDevices.as_view(), name='list_devices'),
    path('add-device/', CreateDevice.as_view(), name='add_device_form'),
    path('detail/<uuid:pk>/<slug:timestamp>', DetailDevice.as_view(), name='detail_device'),
    path('integrate', Integration.as_view(), name='integration'),
    path('signup/', signup_view, name="signup")
]