from rest_framework import serializers
from .models import Skill, Resume, BusinessProfile, GovtProfile

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

class ResumeSerializer(serializers.ModelSerializer):
    # This nests the full skill object in the resume JSON
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Resume
        fields = ['id', 'location', 'bio', 'availability', 'is_verified', 'user', 'skills']

class BusinessProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = '__all__'

class GovtProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovtProfile
        fields = '__all__'