from django.contrib import admin
from my_test_app.models import User, Lesson, Product, VideoWatch


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'url_adress', 'length',)
    fields = ('name', 'url_adress', 'length',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner',)
    fields = ('name', 'owner', 'accesses', 'lessons')


@admin.register(VideoWatch)
class VideoWatchAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'time_stop', 'is_watched')
    fields = ('user', 'lesson', 'time_stop', 'is_watched')
