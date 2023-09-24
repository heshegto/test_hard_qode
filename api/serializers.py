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


class ProductStatisticsSerializer(serializers.ModelSerializer):
    amount_of_watched_videos = serializers.SerializerMethodField('_amount_of_watched_videos')

    class Meta:
        model = Product
        fields = ('id', 'name', 'owner', 'amount_of_watched_videos')


    def _amount_of_watched_videos(self, obj):
        lessons = obj.lessons.all()
        # print(lesson)
        # lesson__in = obj.lessons
        return VideoWatch.objects.filter(is_watched=True, lesson__in=lessons).aggregate(Count('lesson'))
