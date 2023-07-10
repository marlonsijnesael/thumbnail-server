from rest_framework import serializers
from .models import TextureImage, Project


class TextureSerializer(serializers.ModelSerializer):

    image_url = serializers.SerializerMethodField('get_image_url')
    thumbnail_url = serializers.SerializerMethodField('get_thumbnail_url')

    @staticmethod
    def get_image_url(texture):
        if texture.image:
            return texture.image.url
        return ''

    @staticmethod
    def get_thumbnail_url(texture):
        if texture.thumbnail:
            return texture.thumbnail.url
        return ''

    class Meta:
        model = TextureImage
        fields = ['id', 'title', 'description', 'image_url', 'image', 'thumbnail', 'thumbnail_url']


class ProjectSerializer(serializers.ModelSerializer):
    scene_url = serializers.SerializerMethodField('get_scene_url')

    @staticmethod
    def get_scene_url(project):
        if project.scene:
            return project.scene.url
        return ''

    class Meta:
        model = Project
        fields = ['id', 'name', 'scene', 'scene_url']
