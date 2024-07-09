from rest_framework import serializers
from .models import Post

# Serializer for the Post model
# This class is responsible for converting Post instances into JSON data and validating incoming data for creating or updating posts.


class PostSerializer(serializers.ModelSerializer):

    # Meta class specifies the model and fields to be used by the serializer.
    class Meta:
        # The model associated with this serializer. It tells DRF which model the serializer will be handling.
        model = Post
        # Specifies that all fields from the model should be included in the serialization and deserialization process.
        fields = "__all__"
