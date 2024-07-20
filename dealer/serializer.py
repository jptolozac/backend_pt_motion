from rest_framework import serializers
from .models import *

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['name']

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['name']

class DealerSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    branch = BranchSerializer(read_only=True)
    applicant = ApplicantSerializer(read_only=True)
    brand_name = serializers.CharField(write_only=True)
    branch_name = serializers.CharField(write_only=True)
    applicant_name = serializers.CharField(write_only=True)

    class Meta:
        model = Dealer
        fields = ['id', 'brand', 'branch', 'applicant', 'brand_name', 'branch_name', 'applicant_name']

    def create(self, validated_data):
        brand_name = validated_data.pop('brand_name')
        branch_name = validated_data.pop('branch_name')
        applicant_name = validated_data.pop('applicant_name')

        brand, _ = Brand.objects.get_or_create(name=brand_name)
        branch, _ = Branch.objects.get_or_create(name=branch_name)
        applicant, _ = Applicant.objects.get_or_create(name=applicant_name)

        dealer = Dealer.objects.create(
            brand=brand,
            branch=branch,
            applicant=applicant,
            **validated_data
        )
        return dealer
    
    def update(self, instance, validated_data):
        brand_name = validated_data.pop('brand_name', None)
        branch_name = validated_data.pop('branch_name', None)
        applicant_name = validated_data.pop('applicant_name', None)

        if brand_name:
            brand, _ = Brand.objects.get_or_create(name=brand_name)
            instance.brand = brand

        if branch_name:
            branch, _ = Branch.objects.get_or_create(name=branch_name)
            instance.branch = branch

        if applicant_name:
            applicant, _ = Applicant.objects.get_or_create(name=applicant_name)
            instance.applicant = applicant

        instance.save()
        return instance

