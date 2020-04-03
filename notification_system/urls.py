from django.urls import path
from .views import DeviceView, UserCreate, LoginView


app_name = 'api'

urlpatterns = [
    path('report/<uuid:pk>/',  DeviceView.as_view(), name='report-api'),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
]