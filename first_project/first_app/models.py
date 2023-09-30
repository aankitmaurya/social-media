from django.db import models
import uuid
from django.db.models import JSONField
# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=128)
    qualification = models.CharField(max_length=1024, null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Students(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024, null=True, blank=True)
    roll_number = models.IntegerField(null=True, blank=True)
    mobile_number = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True, max_length=128)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        indexes = [
            models.Index(fields=['name']),
        ]


class ClassRoom(models.Model):
    name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True, blank=True)
    student = models.ManyToManyField(Students, blank=True, related_name="classroom_students")
    description = models.CharField(max_length=1024, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.SET_NULL)
    extra_data = JSONField(null=True, blank=True)

    def __str__(self):
        return self.name
