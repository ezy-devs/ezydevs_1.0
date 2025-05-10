from django.db import models
import uuid
# Create your models here.
from django.contrib.auth.models import User

class Testimonies(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return self.name
class Services(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100)  # Assuming you're using FontAwesome or similar
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title
class Projects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title
class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')
    bio = models.TextField()
    social_links = models.JSONField(default=dict, blank=True)  # Store social media links as JSON
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name