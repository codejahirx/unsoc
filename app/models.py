import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class CustomUser(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user_name = models.CharField(max_length=255)
    user_social_id = models.CharField(max_length=20, unique=True)
    email_address = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    contact_number = models.CharField(max_length=15, unique=True)
    registered_date = models.DateTimeField(default=timezone.now)
    account_suspended = models.BooleanField(default=False)
    account_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name
