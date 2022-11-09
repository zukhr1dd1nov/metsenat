from django.shortcuts import render
from rest_framework import viewsets
from .models import SponsorModel
from .serializer import SponsorSerializer

class SponsorDetailView(viewsets.ReadOnlyModelViewSet):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorSerializer