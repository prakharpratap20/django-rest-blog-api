from rest_framework import generics
from ..serializers import CommentSerializer
from ..services.comment_service import CommentService
from rest_framework.exceptions import NotFound


class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs("post_id")
        return CommentService.get_comments_by_post_id(post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        CommentService.create_comment(serializer.validated_data, post_id)


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer

    def get_object(self):
        post_id = self.kwargs.get("post_id")
        comment_id = self.kwargs.get("comment_pk")
        comment = CommentService.get_common_by_post_and_id(post_id, comment_id)
        if comment is None:
            raise NotFound("Comment not found.")
        return comment

    def perform_update(self, serializer):
        comment_id = self.kwargs["comment_pk"]
        CommentService.update_comment(serializer.validated_data, comment_id)

    def perform_destroy(self, instance):
        comment_id = self.kwargs["comment_pk"]
        CommentService.delete_comment(comment_id)
