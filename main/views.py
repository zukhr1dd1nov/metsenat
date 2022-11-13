from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .models import Sponsor, Student
from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, AllowAny


class MainListView(APIView):
    def get(self, request):
        qs = Sponsor.objects.all()
        if self.request.query_params:
            params=self.request.query_params
            if params['sp-flnm']:
                qs.filter(full_name__icontains=params['sp-flnm'])
            if params['sp-cond']:
                qs.filter(condition=params['sp-cond'])
            if params['sp-b']:
                qs.filter(budget=params['sp-b'])
            if params['sp-bg']:
                qs.filter(budget__gte=params['sp-bg'])
            if params['sp-be']:
                qs.filter(budget__lte=params['sp-bg'])
        serializer_sponsor = SponsorSerializer(qs, many=True)

        qs = Student.objects.all()
        serializer_student = StudentSerializer(qs, many=True)

        return Response({
            'sponsors': serializer_sponsor.data,
            'students': serializer_student.data
        }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SponsorCreateView(generics.CreateAPIView):
    queryset = Sponsor
    serializer_class = SponsorCreateSerializer
    permission_classes = [AllowAny]


class SponsorDetailView(generics.RetrieveUpdateAPIView):
    queryset = Sponsor
    serializer_class = SponsorDetailSerializer


class StudentDetailView(APIView):

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        serializer = StudentSerializer(self.get_object(pk))
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, pk):
        object = self.get_object(pk)
        serializers = StudentDetailSerializer(object, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk):
        request.data['student'] = pk
        serializer = StudentBudgetSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)