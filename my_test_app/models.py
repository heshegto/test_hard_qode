from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


# Задание 1.2
class Lesson(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    url_address = models.URLField(blank=False, null=False)
    # Длина видео урока в секундах
    length_in_seconds = models.PositiveSmallIntegerField(default=0, blank=False, null=False)


# Моя модель пользователя
class User(AbstractUser):
    # Просмотры видео
    video_watches = models.ManyToManyField(
        to='Lesson',
        through="VideoWatch",
        blank=True,
    )
    # Доступные уроки
    accesses = models.ManyToManyField(
        to='Product',
        related_name='access',
        blank=True,
    )


# Задание 1.1
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


# Задание 1.3
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

    def save(self, *args, **kwargs):
        if self.time_stop >= 0.8:
            self.is_watched = True
        else:
            self.is_watched = False
        super().save(*args, **kwargs)
