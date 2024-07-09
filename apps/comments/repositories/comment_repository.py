from ..models import Comment


class CommentRepository:
    @staticmethod
    def get_comments_by_post_id(post_id):
        # retrieve all comments associated with a specific post_id
        return Comment.objects.filter(post=post_id)

    @staticmethod
    def get_comment_by_post_and_id(post_id, comment_id):
        # retrieve a specific comment by post_id and comment_id
        try:
            return Comment.objects.get(post_id=post_id, id=comment_id)
        except Comment.DoesNotExist:
            # return none if no comment is found
            return None

    @staticmethod
    def create_comment(data, post_id):
        # create a new comment associated with a specific post_id
        return Comment.objects.create(post_id=post_id, **data)

    @staticmethod
    def update_comment(data, comment_id):
        # update an existing comment identified by comment_id
        comment = Comment.objects.get(pk=comment_id)
        for attr, value in data.items():
            setattr(comment, attr, value)
        comment.save()
        return comment

    @staticmethod
    def delete_comment(comment_id):
        # delete an existing comment identified by comment_id
        comment = Comment.objects.get(pk=comment_id)
        comment.delete()
