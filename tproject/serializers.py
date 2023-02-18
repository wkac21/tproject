from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    thumbnail_200 = serializers.SerializerMethodField()
    thumbnail_400 = serializers.SerializerMethodField()
    original_url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ('id', 'owner', 'image', 'thumbnail_200', 'thumbnail_400', 'original_url', 'expiration_time')
        read_only_fields = ('owner', 'thumbnail_200', 'thumbnail_400', 'original_url', 'expiration_time')

    def get_thumbnail_200(self, obj):
        if obj.thumbnail_200:
            return self.context['request'].build_absolute_uri(obj.thumbnail_200.url)
        return None

    def get_thumbnail_400(self, obj):
        if obj.thumbnail_400:
            return self.context['request'].build_absolute_uri(obj.thumbnail_400.url)
        return None

    def get_original_url(self, obj):
        if obj.original_url:
            return obj.original_url
        return self.context['request'].build_absolute_uri(obj.image.url)


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = (
        'id', 'name', 'thumbnail_sizes', 'original_url', 'expiring_link', 'expiration_time_min', 'expiration_time_max')


class CustomUserSerializer(serializers.ModelSerializer):
    level = LevelSerializer(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'level')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        level_data = validated_data.pop('level', None)
        user = User.objects.create_user(**validated_data)
        if level_data:
            level = Level.objects.create(**level_data)
            user.level = level
            user.save()
        return user


    def update(self, instance, validated_data):
        level_data = validated_data.pop('level', None)
        if level_data:
            level = instance.level
            if not level:
                level = Level.objects.create()
                instance.level = level
            level.name = level_data.get('name', level.name)
            level.thumbnail_sizes = level_data.get('thumbnail_sizes', level.thumbnail_sizes)
            level.original_url = level_data.get('original_url', level.original_url)
            level.expiring_link = level_data.get('expiring_link', level.expiring_link)
            level.expiration_time_min = level_data.get('expiration_time_min', level.expiration_time_min)
            level.expiration_time_max = level_data.get('expiration_time_max', level.expiration_time_max)
            level.save()
        return super().update(instance, validated_data)
