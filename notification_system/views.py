from websiteapp.models import Device, Measurement
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from .serializers import MeasurementsSerializer, UserSerializer
import datetime
import json


class DeviceView(APIView):

    def valid_request_get(self, request, pk):
        if pk != None:
            device = Device.objects.filter(dev_id=pk)
            if len(device) != 0:
                if request.user == device.get().owner:
                    return True
                    # device and user exist
        return False

    def valid_request_post(self, request_data, pk):
        if request_data.get('token') != None:
            device = Device.objects.filter(dev_id=pk)
            token = Token.objects.filter(key=request_data.get('token'))
            if len(device) != 0 and len(token) != 0:
                if token.get().user == device.get().owner:
                    return True
                # device and user exist
        else:
            return False

    def get(self, request, *args, **kwargs):
        if self.valid_request_get(request, kwargs['pk']):
            measurements = Measurement.objects.filter(device_id=kwargs['pk'])
            serializer = MeasurementsSerializer(measurements, many=True)
        else:
            serializer = MeasurementsSerializer(Measurement.objects.none(), many=True)
        return Response({"Measurements": serializer.data})
    
    def post(self, request, *args, **kwargs):
        request_data = request.data
        if self.valid_request_post(request_data, kwargs['pk']):
            measure = request_data.get('data')
            measure['time'] = datetime.datetime.now()
            measure['device_id'] = Device.objects.filter(dev_id=kwargs['pk']).get().dev_id
            serializer = MeasurementsSerializer(data=measure)
            if serializer.is_valid(raise_exception=True):
                measure_saved = serializer.save()
                return Response({"success": "New measurement"})
        else:
                return Response({"error": "Can't POST"})



class UserCreate(generics.CreateAPIView):

    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()



class LoginView(APIView):

    permission_classes = ()
    authentication_classes = ()

    def post(self, request,):
        username = str(request.data.get("username"))
        password = str(request.data.get("password"))
        user = authenticate(username=username, password=password)
        token = Token.objects.get_or_create(user=user)
        if user:
            return Response({"token": str(token[0])})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)