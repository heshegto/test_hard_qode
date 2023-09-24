from rest_framework import serializers
from my_test_app.models import User, Product, Lesson, Accesses


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'name', 'url_address', 'length_in_seconds')


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
