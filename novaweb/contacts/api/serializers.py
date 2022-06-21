from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from contacts.models import Contact


class ContactSerializer(ModelSerializer):
    phones = serializers.StringRelatedField(many=True)

    class Meta:
        model = Contact
        fields = ['id','name', 'email', 'phones']