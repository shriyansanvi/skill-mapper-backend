from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResumeViewSet, SkillViewSet, BusinessProfileViewSet, GovtProfileViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'resumes', ResumeViewSet, basename='resume')
router.register(r'skills', SkillViewSet, basename='skill')
router.register(r'businesses', BusinessProfileViewSet, basename='businessprofile')
router.register(r'govt', GovtProfileViewSet, basename='govtprofile')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]