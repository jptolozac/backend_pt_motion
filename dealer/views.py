# from django.shortcuts import render
from rest_framework import viewsets
from .serializer import DealerSerializer
from .models import Dealer

# Create your views here.
class DealerView(viewsets.ModelViewSet):
    serializer_class = DealerSerializer
    queryset = Dealer.objects.all()