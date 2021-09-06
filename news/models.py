from django.db import models
from django.contrib.auth import get_user_model
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify
from six import python_2_unicode_compatible
from PIL import Image

@python_2_unicode_compatible
class Post(models.Model):
    AI= "AI"
    SPACE_RELATED= 'Space'
    ROBOTICS= 'Robotics'
    GENERAL= 'General'
    category_choices= [
        (AI, 'Artificial Intelligence'),
        (SPACE_RELATED, 'Space related'),
        (ROBOTICS, 'Robotics'),
        (GENERAL, 'General'),
    ]
    posted_by= models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')
    title= models.CharField(max_length=150)
    content= models.TextField(null=True, blank=True)
    date_of_publication= models.DateTimeField(auto_now_add= True)
    category= models.CharField(max_length=50, choices=category_choices, default=GENERAL)
    image1= models.ImageField(null= False, blank= False, upload_to= 'post_photo/')
    slug= models.SlugField(unique=True, null=True, blank=True, max_length=50)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', 
        related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()

        if not self.slug:
            self.slug= slugify(self.title)

        return super(Post, self).save(*args, **kwargs)