from django.contrib import admin
from my_test_app.models import User, Lesson, Product, VideoWatch


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    fields = (('username', 'password'), 'user_permissions', 'accesses')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'url_address', 'length_in_seconds',)
    fields = ('name', 'url_address', 'length_in_seconds',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner',)
    fields = ('name', 'owner', 'lessons')


@admin.register(VideoWatch)
class VideoWatchAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'time_stop', 'is_watched')
    fields = ('user', 'lesson', 'time_stop', 'is_watched')
