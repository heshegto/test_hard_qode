from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class Lesson(models.Model):
    name = models.CharField(max_length=128)
    url_adress = models.URLField()
    length = models.TimeField()


class User(AbstractUser):
    video_watch = models.ManyToManyField(to=Lesson, through="VideoWatch")


class Product(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='owner')
    accesses = models.ManyToManyField(User, related_name='access')
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
