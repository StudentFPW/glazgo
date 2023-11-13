from rest_framework import serializers

from .models import *


class CPHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CPHistory
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class ResponsibilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsibilities
        fields = "__all__"


class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = "__all__"


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"


class CPromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidatePromotion
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
