from phones.models import Phone
from phones.api.serializers import PhoneSerializer
from rest_framework.viewsets import ModelViewSet


class PhoneViewSet(ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer