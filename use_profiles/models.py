from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profiles_images/', blank=True)

    def __unicode__(self):
        return self.user.username

# Create your models here.