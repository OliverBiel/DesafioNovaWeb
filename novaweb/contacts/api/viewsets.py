from contacts.models import Contact
from contacts.api.serializers import ContactSerializer
from rest_framework.viewsets import ModelViewSet


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer