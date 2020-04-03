from django import forms
from .models import Device
    
class AddDeviceForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = ['title', 'serial_number', 'quantity']    
