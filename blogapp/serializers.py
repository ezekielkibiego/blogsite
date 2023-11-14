from dataclasses import fields
from rest_framework import serializers
from .models import *

class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    editor = EditorSerializer()
    class Meta:
        model = Blog
        fields = '__all__'

    def create(self, validated_data):
        editor_data = validated_data.pop('editor')

        editor = Editor.objects.create(**editor_data)

        blog = Blog.objects.create(editor=editor, **validated_data)

        return blog

