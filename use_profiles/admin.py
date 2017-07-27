from django.contrib import admin

# Register your models here.
from use_profiles.models import  UserProfile

admin.site.register(UserProfile)
