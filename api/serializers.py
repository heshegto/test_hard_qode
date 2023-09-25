from rest_framework import serializers
from my_test_app.models import User, Product, Lesson, Accesses, VideoWatch
from django.db.models import Count


class VideoWatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoWatch
        fields = ('time_stop', 'is_watched', 'lesson')


class LessonSerializer(serializers.ModelSerializer):
    video_watch_data = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ('id', 'name', 'url_address', 'length_in_seconds', 'video_watch_data')

    def get_video_watch_data(self, obj):
        selected_options = VideoWatch.objects.filter(
            lesson=obj.pk,
            user=self.context['request'].user
        )
        return VideoWatchSerializer(selected_options, many=True).data


class ProductSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'owner', 'lessons')


class AccessesSerializer(serializers.ModelSerializer):
    accesses = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Accesses
        fields = ('accesses',)


class UserSerializer(serializers.ModelSerializer):
    accesses = AccessesSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'accesses')


# Нужно только для задания 2.3
class ProductStatisticsSerializer(serializers.ModelSerializer):
    amount_of_watched_videos = serializers.SerializerMethodField('_amount_of_watched_videos')
    sum_of_spent_time = serializers.SerializerMethodField('_sum_of_spent_time')
    amount_of_current_users = serializers.SerializerMethodField('_amount_of_current_users')
    amount_of_sold_products = serializers.SerializerMethodField('_amount_of_sold_products')

    class Meta:
        model = Product
        fields = ('id', 'name', 'owner', 'amount_of_watched_videos', 'sum_of_spent_time', 'amount_of_current_users', 'amount_of_sold_products')

    # Задание 2.3a
    def _amount_of_watched_videos(self, obj):
        lessons = obj.lessons.all()
        return VideoWatch.objects.filter(
                    is_watched=True,
                    lesson__in=lessons
                ).aggregate(Count('lesson'))['lesson__count']

    # Задание 2.3b
    def _sum_of_spent_time(self, obj):
        lessons_id = obj.lessons.all()
        video_watches = VideoWatch.objects.filter(lesson__in=lessons_id)
        result = 0
        for vw in video_watches:
            result += vw.time_stop * vw.lesson.length_in_seconds
        return result

    # Задание 2.3c
    def _amount_of_current_users(self, obj):
        lessons_id = obj.lessons.all()
        return VideoWatch.objects.filter(
                    is_watched=False,
                    lesson__in=lessons_id
                ).values('user').distinct().aggregate(Count('user'))['user__count']

    # Задание 2.3d
    def _amount_of_sold_products(self, obj):
        return Accesses.objects.filter(accesses=obj).aggregate(Count('user'))['user__count']
