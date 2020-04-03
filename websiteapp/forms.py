from django import forms
from .models import Device
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
    
class AddDeviceForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = ['title', 'serial_number', 'quantity', 'border_value']    


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
