from django.views.generic import ListView, DetailView
from ..models import Comment
from ..services.comment_service import CommentService


class CommentListView(ListView):
    model = Comment
    template_name = "comments/comment_list.html"
    context_object_name = "comments"

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        return CommentService.get_comments_by_post_id(post_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_id"] = self.kwargs.get("post_id")
        return context


class CommentDetailView(DetailView):
    model = Comment
    template_name = "comments/comment_detail.html"
    context_object_name = "comment"

    def get_object(self, queryset=None):
        post_id = self.kwargs.get("post_id")
        comment_id = self.kwargs.get("comment_id")
        return CommentService.get_comment_by_post_and_id(post_id, comment_id)
