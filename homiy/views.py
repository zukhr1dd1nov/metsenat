from django.shortcuts import render
from user.models import SponsorModel
from rest_framework import generics
from user.serializer import SponsorCreateSerializer, SponsorDetailSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class SponsorCreateView(generics.CreateAPIView):
    queryset = SponsorModel
    serializer_class = SponsorCreateSerializer


class SponsorDetailView(generics.RetrieveUpdateAPIView):
    queryset = SponsorModel
    serializer_class = SponsorDetailSerializer
