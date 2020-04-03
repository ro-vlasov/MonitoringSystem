from django.shortcuts import render
from django.core.mail import send_mail
from .models import MailTimeBase
from rest_framework.authtoken.models import Token
from datetime import datetime, timedelta, timezone


def notificate(token, device, measure, email):
    title = "The device '" + device.title + "' displays strange values!"
    data_msg = """\
Good day, %s! Please, check you device %s.\n \
It displays strange value: (value=%s, time=%s) \
""" % (device.owner, device.title , measure['value'], measure['time'])
    user = Token.objects.get(key=token).user
    query = MailTimeBase.objects.get(user=user)
    if query == MailTimeBase.objects.none():
        query = MailTimeBase.objects.create(user=user, time=datetime.now(timezone.utc))
    mailtimeobj = query
    now = datetime.now(timezone.utc)
    if now - mailtimeobj.time >= timedelta(minutes=5):
        mailtimeobj.time = datetime.now(timezone.utc)
        mailtimeobj.save()
        send_mail(title, data_msg, "Monitoring System written by Roman Vlasov", [email], fail_silently=False)