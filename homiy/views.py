from django.shortcuts import render
from user.models import SponsorModel
from rest_framework import generics
from user.serializer import SponsorCreateSerializer


class SponsorCreateView(generics.CreateAPIView):
    queryset = SponsorModel
    serializer_class = SponsorCreateSerializer
