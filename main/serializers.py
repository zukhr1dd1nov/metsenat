from django.db.models import F
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
import  re
from .models import University, Sponsor, Student, StudentBudget


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        exclude = ['updated_at', 'used']


class SponsorCreateSerializer(serializers.ModelSerializer):
    condition = serializers.HiddenField(default=1)

    class Meta:
        model = Sponsor
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
        if re.match(r'(9[^26]|71)\d{7}', validated_data.get('phone')):
            errors['full_name'] = "Iltimos Familiya Ism Sharifingizni to'liq va haqiqatta yozing"
        if errors:
                raise ValidationError(errors)
        return Sponsor.objects.create(**validated_data)


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'


class SponsorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'
        read_only_fields = ['full_name', 'person', 'phone', 'name_company', 'budget']


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['name']


class StudentSerializer(serializers.ModelSerializer):
    # university = University3Serializer()

    class Meta:
        model = Student
        exclude = ['created_at', 'updated_at']


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
        sponsor.used += money
        sponsor.save()
        student.send += money
        student.save()
        return StudentBudget.objects.create(**validated_data)


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
