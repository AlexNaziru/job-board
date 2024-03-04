# This is so we convert data into JSON
from rest_framework import serializers
from .models import Job, Category


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
        )


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'id',
            'title',
            'position_salary',
            'position_location',
            'company_name',
            'created_at_formatted'
        )


class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'id',
            'category',
            'title',
            'description',
            'position_salary',
            'position_location',
            'company_name',
            'company_location',
            'company_email',
            'created_at_formatted',
        )
