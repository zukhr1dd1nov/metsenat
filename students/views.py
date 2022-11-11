from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import StudentModel, StudentBudgetModel
from rest_framework import generics, status
from user.serializer import StudentSerializer, StudentBudgetSerializer, StudentDetailSerializer


class StudentListView(generics.ListAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer


class StudentCreateView(generics.CreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer


class StudentBudgetView(generics.CreateAPIView):
    queryset = StudentBudgetModel.objects.all()
    serializer_class = StudentBudgetSerializer


class StudentDetailView(APIView):

    def get_object(self, pk):
        try:
            return StudentModel.objects.get(pk=pk)
        except StudentModel.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        serializer = StudentSerializer(self.get_object(pk))
        return Response(serializer.data)

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
