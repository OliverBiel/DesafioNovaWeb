from contacts.models import Contact
from phones.models import Phone
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class PhoneSerializer(ModelSerializer):
    class Meta:
        model = Phone
        fields = ['number', 'contacts']