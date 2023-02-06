from rest_framework import serializers
from . import models

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        # exclude = ['updated_at',] #used this untill want to get all data
        fields = ['blog_title', 'uuid']

class BlogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        exclude = ['updated_at',] #used this untill want to get all data
        