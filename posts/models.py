from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField
from django.db import models

"""
Publish Manager
"""
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                    self).get_queryset()\
                .filter(status='published')
   
"""
Category Model
"""
class Category(models.Model):
    pass

"""
Post Model
"""
class Post(models.Model):
    POST_STATUS_CHOICES = (
        ('1', 'Project'),
        ('2', 'Published'),
    )
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='2')
    body = RichTextField(blank=True, null=True)
    cover_img = models.ImageField(upload_to='cover_img/', blank=True)