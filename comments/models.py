from django.db import models
from django.contrib.auth import get_user_model
from news.models import Post
import uuid

class Comment(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    commentedby= models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    under_the_post= models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content_of_comment= models.TextField(null=False, blank=False)
    commented_in= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.under_the_post.title