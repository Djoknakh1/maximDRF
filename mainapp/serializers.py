from rest_framework import serializers

from mainapp.models import Vacancy, Employer, Area, Salary, Currency, Address, Snippet


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class SalarySerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()

    class Meta:
        model = Salary
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):
    employer = EmployerSerializer()
    area = AreaSerializer()
    salary = SalarySerializer()
    address = AddressSerializer()
    snippet = SnippetSerializer()

    class Meta:
        model = Vacancy
        fields = '__all__'
