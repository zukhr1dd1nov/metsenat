from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import UniversityModel, SponsorModel, StudentModel, StudentBudgetModel


class SponsorCreateSerializer(serializers.ModelSerializer):

    condition = serializers.HiddenField(default=1)

    class Meta:
        model = SponsorModel
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data.get('person'), validated_data.get('name_company')=='')
        if (validated_data.get('person') == 0 and validated_data.get('name_company') == '') or (
                validated_data.get('person') == 1 and validated_data.get('name_company') != ''):
            raise ValidationError("Yuridik shaxsning firma nomi bo'lishi shart")
        return SponsorModel.objects.create(**validated_data)

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
