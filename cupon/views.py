from django.shortcuts import render
from .models import Cupon
from .serializers import CuponSerializer
from rest_framework import  viewsets
# Create your views here.


class CuponViewSet(viewsets.ModelViewSet):
    serializer_class = CuponSerializer

    def get_queryset(self):
        cupons = Cupon.objects.all()
        return cupons