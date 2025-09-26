from rest_framework import viewsets
from .models import Skill, Resume, BusinessProfile, GovtProfile
from .serializers import SkillSerializer, ResumeSerializer, BusinessProfileSerializer, GovtProfileSerializer

# A ViewSet for viewing resumes. ReadOnly means it can't be modified through the API yet.
class ResumeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class BusinessProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BusinessProfile.objects.all()
    serializer_class = BusinessProfileSerializer

class GovtProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GovtProfile.objects.all()
    serializer_class = GovtProfileSerializer