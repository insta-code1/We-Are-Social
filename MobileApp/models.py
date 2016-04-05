from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):

    class Meta: #include this to ensure build in IDE
        app_label="MobileApp"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return "Yo It's " + self.first_name