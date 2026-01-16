from rest_framework import serializers
from django.templatetags.static import static
from .models import Home, About, ContactMessage, Project


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = "__all__"
    
    def get_image(self, obj):
        # Convert media path to static path
        # From: projects/Screenshot_2025-12-19_164425.png
        # To: portfolio/images/projects/Screenshot_2025-12-19_164425.png
        if obj.image:
            filename = str(obj.image).replace('projects/', '')
            static_path = f'portfolio/images/projects/{filename}'
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(static(static_path))
            return static(static_path)
        return None