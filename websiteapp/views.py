from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Device, Measurement
from django.shortcuts import render
from .forms import AddDeviceForm
import datetime
import json

class ListDevices(LoginRequiredMixin, ListView):
    template_name = 'list_devices.html'
    model = Device

    def get_queryset(self):
        return Device.objects.filter(owner=self.request.user).order_by('serial_number')

class CreateDevice(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = AddDeviceForm()
        context = {'form': form}
        return render(request, 'add_device.html', context)

    def post(self, request, *args, **kwargs):
        form = AddDeviceForm(data=request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.owner = request.user
            device.save()
            return redirect('websiteapp:list_devices')
        return render(request, 'add_device.html', {'form': form})


class DetailDevice(LoginRequiredMixin, DetailView):
    template_name = 'device_detail.html'
    model = Device

    def define_timestamp(self):
        if 'timestamp' in self.kwargs.keys():
            timest = self.kwargs['timestamp'].lower()
            if timest == 'hour':
                return (datetime.datetime.now() - datetime.timedelta(hours=1), 'hour')
            if timest == 'day':
                return (datetime.datetime.now() - datetime.timedelta(days=1), 'day')
            if timest == 'week':
                return (datetime.datetime.now() - datetime.timedelta(weeks=1), 'week')
        return (None, 'All the time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        timestamp = self.define_timestamp()
        if timestamp[0] != None:
            queryset = Measurement.objects.filter(device_id=self.kwargs['pk'], time__gt=timestamp[0]).values_list('time', 'value')
            context['timeperiod'] = timestamp[1]
        else:
            queryset = Measurement.objects.filter(device_id=self.kwargs['pk']).values_list('time', 'value')
            context['timeperiod'] = timestamp[1]
        context['times'] = json.dumps([obj[0] for obj in queryset], default=str)
        context['values'] = json.dumps([obj[1] for obj in queryset])
        context['device'] = Device.objects.filter(dev_id=self.kwargs['pk']).get()
        context['total_measures'] = len(queryset)
        return context
 

class Integration(LoginRequiredMixin, View):
    template_name = 'integration.html'

    def get(self, request):
        token = request.user.auth_token.key
        date_dict = {'token': token}
        return render(request, 'integration.html', context=date_dict)
