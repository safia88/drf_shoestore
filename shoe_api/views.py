from rest_framework import viewsets
from django.shortcuts import render
from .serializer import ShoeSerializer, ShoeTypeSerializer, ShoeColorSerializer, ManufacturerSerializer
from .models import Shoe, ShoeType, ShoeColor, Manufacturer


# Create your views here.

def index(request):
    return render(request, 'index.html', {'data': Shoe.objects.all()})


class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer


class ShoeTypeViewSet(viewsets.ModelViewSet):
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer


class ShoeColorViewSet(viewsets.ModelViewSet):
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
