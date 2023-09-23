from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class Lesson(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    url_adress = models.URLField(unique=True, blank=False, null=False)
    length_in_seconds = models.PositiveSmallIntegerField(default=0, blank=False, null=False)


class User(AbstractUser):
    video_watch = models.ManyToManyField(to=Lesson, through="VideoWatch")
    accesses = models.ManyToManyField('Product', related_name='access', blank=True)


class Product(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='owner')
    lessons = models.ManyToManyField(Lesson)


class VideoWatch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    time_stop = models.FloatField(
        default=0.0,
        validators=[
            MaxValueValidator(1.0),
            MinValueValidator(0.0)
        ]
    )
    is_watched = models.BooleanField(default=False)
