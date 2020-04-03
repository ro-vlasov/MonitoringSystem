from django.db import models
from django.contrib.auth.models import User

class MailTimeBase(models.Model):

    time = models.DateTimeField(
        null=True,
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    
    def __str__(self):
        return ' '.join([str(self.time), str(self.user)])