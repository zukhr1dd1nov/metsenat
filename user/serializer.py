from rest_framework import serializers
from rest_framework.exceptions import ValidationError
import  re
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
        errors = {}
        if validated_data.get('person') == 0 and validated_data.get('name_company') == '':
            errors['person'] = "Yuridik shaxsning firma nomi bo'lishi shart"
        if validated_data.get('budget') < 1000000:
            errors['budget'] = "Summa kam. Minimal summa 1000000 so'm"
        if validated_data.get('person') == 1 and validated_data.get('name_company') != '':
            errors['person'] = "Jismoniy shaxsning firma nomi bo'lmaydi"
        if len(validated_data.get('full_name').split())!=3 or not ''.join(validated_data.get('full_name').split()).isalpha():
            errors['full_name'] = "Iltimos Familiya Ism Sharifingizni to'liq va haqiqatta yozing"
        if re.match(r'(9[^26]|71)\d{7}', validated_data.get('phone_number')):
            errors['full_name'] = "Iltimos Familiya Ism Sharifingizni to'liq va haqiqatta yozing"
        if errors:
                raise ValidationError(errors)
        return SponsorModel.objects.create(**validated_data)

class SponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = SponsorModel
        fields = '__all__'


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
