from django.db import models
from contacts.models import Contact


class Phone(models.Model):
    number = models.CharField(max_length=75)
    contacts = models.ForeignKey(Contact, related_name='phones', on_delete=models.CASCADE)

    def __str__(self):
        return self.number