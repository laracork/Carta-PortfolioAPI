from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from . models import Investments
from . serializers import InvestmentsSerializer
from django_filters import rest_framework as filters

class InvestmentsFilter(filters.FilterSet):
    """
    Parameters that allow data to be filtered by date
    """
    buy_date = filters.CharFilter(lookup_expr='icontains')
    sell_date = filters.CharFilter(lookup_expr='icontains')
    updated_date = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Investments
        fields = ('buy_date', 'sell_date', 'updated_date',)

class InvestmentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that provides CRUD methods for Investments Model
    """
    queryset = Investments.objects.all().order_by('-buy_date',)
    serializer_class = InvestmentsSerializer
    filterset_class = InvestmentsFilter
