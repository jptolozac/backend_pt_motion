# from django.shortcuts import render
from rest_framework import viewsets
from .serializer import DealerSerializer
from .models import Dealer

# Create your views here.
class DealerView(viewsets.ModelViewSet):
    serializer_class = DealerSerializer
    queryset = Dealer.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get('ordering', 'id')
        return queryset.order_by(ordering)