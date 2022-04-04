from tabnanny import verbose
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
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
class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_('Name'), max_length=255),
        slug=models.SlugField(_('Slug'), max_length=255),
    )

    class Meta:
        verbose_name = _('category')
        verbose_name_plura = _('categories')

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)
    
    def get_absolute_url(self):
        return reverse('posts:posts_by_category', args=[self.id, self.slug])


"""
Post Model
"""
class Post(TranslatableModel):
    POST_STATUS_CHOICES = (
        ('1', 'Project'),
        ('2', 'Published'),
        ('3', 'Archived'),
    )
    translations = TranslatedFields(
        title=models.CharField(_('Title'), max_length=255),
        slug=models.SlugField(_('Slug'), max_length=255),
        body=RichTextField(_('Body'), blank=True, null=True),
    )
    category = models.ForeignKey(_('Category'), Category, related_name='posts', on_delete=models.CASCADE)
    author = models.ForeignKey(_('Author'), User, on_delete=models.CASCADE)
    cover_img = models.ImageField(_('Cover Image'), upload_to='cover_img/', blank=True)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True)
    status = models.CharField(_('Status'), max_length=20, choices=POST_STATUS_CHOICES, default='1')
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

    def get_absolute_url(self):
        return reverse('posts:post_detail', args=[self.id, self.slug])