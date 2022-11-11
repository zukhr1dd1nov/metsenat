from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import SponsorModel, StudentModel
from .serializer import SponsorSerializer, StudentSerializer
from rest_framework.views import APIView

class ListSponsorView(APIView):
    def get(self, request):
        qs = SponsorModel.objects.all()
        serializer_sponsor = SponsorSerializer(qs, many=True)

        return Response({
            'sponsor': serializer_sponsor.data,
        })