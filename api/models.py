from django.db import models
from django.contrib.auth.models import User

# A separate model for skills to allow for easy searching and filtering.
class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# This is your "Resume Model" for the skilled woman.
class Resume(models.Model):
    AVAILABILITY_CHOICES = [
        ('full-time', 'Full-Time'),
        ('part-time', 'Part-Time'),
        ('project-based', 'Project-Based'),
    ]

    # Links this profile to a specific login account.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='part-time')
    is_verified = models.BooleanField(default=False)
    
    # A resume can have many skills, and a skill can be on many resumes.
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.user.username

# This is your "Business Profile Model".
class BusinessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    industry = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=200)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.company_name

# This is your "Govt Profile Model".
class GovtProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=200)
    jurisdiction = models.CharField(max_length=100) # e.g., 'District Level', 'State Level'
    contact_person = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.department_name
