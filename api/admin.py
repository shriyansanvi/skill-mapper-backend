from django.contrib import admin
from .models import Skill, Resume, BusinessProfile, GovtProfile

# Register your models here to make them visible in the admin panel.
admin.site.register(Skill)
admin.site.register(Resume)
admin.site.register(BusinessProfile)
admin.site.register(GovtProfile)
