from rest_framework import serializers
from .models import Comment

# CommentSerializer is a ModelSerializer that automatically creates fields and methods for the Comment model.


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment  # The model that this serializer will be based on.
        # Automatically include all fields from the Comment model.
        fields = "__all__"
