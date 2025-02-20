from django.db import models
from django.utils import timezone
import uuid
from datetime import datetime, date, timedelta

from .validators import comma_separated_validator  
from django.contrib import admin
# OtherModel stays the same
class OtherModel(models.Model):
    name = models.CharField(max_length=255, default="mame")
    id = models.AutoField(primary_key=True)

# In your models.py
class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    fathername = models.TextField(default="mama")
    big_integer_field = models.BigIntegerField(default=123)
    boolean_field = models.BooleanField(default=False)
    char_field = models.CharField(max_length=255, default='Default Value')
    comma_separated_field = models.CharField(
        validators=[comma_separated_validator], max_length=255, default='value1,value2,value3'
    )
    date_field = models.DateField(default=date.today)
    date_time_field = models.DateTimeField(default=timezone.now)  # Use timezone.now directly
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    duration_field = models.DurationField(default=timedelta(days=1))
    email_field = models.EmailField(default='default@example.com')
    file_field = models.FileField(upload_to='upload/',null=True, blank=True)
    file_path_field = models.FilePathField(path='upload/', default='/path/to/files/default_file.txt')
    float_field = models.FloatField(default=0.0)
    generic_ip_address_field = models.GenericIPAddressField(default='127.0.0.1')
    # image_field = models.ImageField(upload_to='upload/', null=True, blank=True)
    json_field = models.JSONField(default=dict)
    many_to_many_field = models.ManyToManyField(OtherModel, blank=True)
    null_boolean_field = models.BooleanField(null=True, blank=True, default=True)
    positive_big_integer_field = models.PositiveBigIntegerField(default=1)
    positive_integer_field = models.PositiveIntegerField(default=1)
    slug_field = models.SlugField(default='default-slug')
    small_integer_field = models.SmallIntegerField(default=1)
    time_field = models.TimeField(default=timezone.now)  
    url_field = models.URLField(default='http://example.com')
    uuid_field = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name

 
class AssignmentAdmin(admin.ModelAdmin): fieldsets = [
        ('Main Information', {
            'fields': ('title', 'description')
        }),
        ('Additional Information', {
            'fields': ('slug', 'user', 'timestamp')
        }),
    ]

    