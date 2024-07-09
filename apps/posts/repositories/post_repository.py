from ..models import Post


class PostRepository:
    # fetch all posts from the database
    @staticmethod
    def get_all_posts():
        return Post.objects.all()

    # fetch a specific post by its primarty key (id)
    @staticmethod
    def get_post_by_id(post_id):
        return Post.objects.get(pk=post_id)

    # create a new post with the provided data
    @staticmethod
    def create_post(data):
        return Post.objects.create(**data)

    # update an existing post with the provided data
    @staticmethod
    def update_post(data, post_id):
        post = Post.objects.get(pk=post_id)
        for attr, value in data.items():
            setattr(post, attr, value)
        post.save()
        return post

    # delete a post by its primary key (id)
    @staticmethod
    def delete_post(post_id):
        post = Post.objects.get(pk=post_id)
        post.delete()
