from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class Lesson(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    url_address = models.URLField(blank=False, null=False)
    length_in_seconds = models.PositiveSmallIntegerField(default=0, blank=False, null=False)


class User(AbstractUser):
    video_watches = models.ManyToManyField(
        to='Lesson',
        through="VideoWatch",
        blank=True,
    )
    accesses = models.ManyToManyField(
        to='Product',
        related_name='access',
        blank=True,
    )


class Product(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(
        to='User',
        related_name='owner',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    lessons = models.ManyToManyField(
        to='Lesson',
        blank=True,
    )


class VideoWatch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True)
    time_stop = models.FloatField(
        default=0.0,
        validators=[
            MaxValueValidator(1.0),
            MinValueValidator(0.0)
        ]
    )
    is_watched = models.BooleanField(default=False)
