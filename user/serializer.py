from rest_framework import serializers
from .models import UniversityModel, SponsorModel, StudentModel, StudentBudgetModel


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorModel
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = UniversityModel
        fields = '__all__'

class StudentBudgetSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentBudgetModel
        fields = '__all__'