from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import UniversityModel, SponsorModel, StudentModel, StudentBudgetModel


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorModel
        exclude = ['updated_at']


class SponsorCreateSerializer(serializers.ModelSerializer):
    condition = serializers.HiddenField(default=1)

    class Meta:
        model = SponsorModel
        fields = '__all__'

    def create(self, validated_data):
        if (validated_data.get('person') == 0 and validated_data.get('name_company') == '') or (
                validated_data.get('person') == 1 and validated_data.get('name_company') != ''):
            raise ValidationError("Yuridik shaxsning firma nomi bo'lishi shart")
        return SponsorModel.objects.create(**validated_data)


class SponsorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorModel
        fields = '__all__'
        read_only_fields = ['full_name', 'person', 'phone_number', 'name_company', 'budget']


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityModel
        fields = ['university_name']


class StudentSerializer(serializers.ModelSerializer):
    # university = University3Serializer()

    class Meta:
        model = StudentModel
        exclude = ['created_at', 'updated_at']


class StudentBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentBudgetModel
        fields = '__all__'


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'
