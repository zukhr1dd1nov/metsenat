from django.db.models import F
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
import re
from .models import University, Sponsor, Student, StudentBudget, LinearGraph
from .tasks import money_management, money_is_needed, money_given


class SponsorCreateSerializer(serializers.ModelSerializer):
    condition = serializers.HiddenField(default=1)

    class Meta:
        model = Sponsor
        exclude = ['updated_at', 'created_at', 'is_counted', 'used']

    def create(self, validated_data):
        errors = {}
        if validated_data.get('is_phisical_person') == 0 and validated_data.get('name_company') == '':
            errors['is_phisical_person'] = "Yuridik shaxsning firma nomi bo'lishi shart"
        if validated_data.get('budget') < 1000000:
            errors['budget'] = "Summa kam. Minimal summa 1000000 so'm"
        if validated_data.get('is_phisical_person') == 1 and validated_data.get('name_company') != '':
            errors['is_phisical_person'] = "Jismoniy shaxsning firma nomi bo'lmaydi"
        if (len(validated_data.get('full_name').split()) != 3) or (not ''.join(validated_data.get('full_name').split()).isalpha()):
            errors['full_name'] = "Iltimos Familiya Ism Sharifingizni to'liq va haqiqatta yozing"
        if not re.match(r'(9[^26]|71)\d{7}', validated_data.get('phone')):
            errors['raqam'] = "Iltimos haqiqiy raqamingizni yozing"
        if errors:
            raise ValidationError(errors)
        return Sponsor.objects.create(**validated_data)


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'
        read_only_fields = ['full_name', 'is_phisical_person', 'phone', 'name_company', 'budget', 'is_counted']

    def update(self, instance, validated_data):
        instance.condition = validated_data.get('condition', instance.condition)
        if instance.is_counted == False and instance.condition == 2:
            instance.is_counted = True
            money_given(instance.budget)
        return instance


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['name']


class StudentSerializer(serializers.ModelSerializer):
    # university = University3Serializer()

    class Meta:
        model = Student
        exclude = ['created_at', 'updated_at']

    def create(self, validated_data):
        money_is_needed(validated_data['request'])
        return Student.objects.create(**validated_data)


class StudentBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentBudget
        fields = '__all__'

    def create(self, validated_data):
        errors = {}
        sponsor = validated_data.get('sponsor')
        student = validated_data.get('student')
        money = validated_data.get('money')
        if sponsor.remaining_budget < money:
            errors['sponsor'] = f"Homiyning puli yetarlicha emas. Homiyda faqatgina {sponsor.remaining_budget} qoldi"
        if student.remaining_request < money:
            errors['student'] = f"Student soralgan puldan ko'proq bo'lishi mumkin emas. Studentga faqatgina {student.remaining_request} kerak"
        if errors:
            raise ValidationError(errors)
        money_management(sponsor, student, money)
        return StudentBudget.objects.create(**validated_data)


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class LinearGraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinearGraph
        fields = '__all__'
        read_only_fields = ['number_sp', 'number_st', 'day']