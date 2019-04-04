from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = {
    ('draft', 'Draft'),
    ('published', 'Published')
    }
    title = models.CharField(_('title'), max_length=250, db_index=True)
    slug = models.SlugField(_('slug'), max_length=250, db_index=True, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    image = models.ImageField(_('image'), upload_to="images/")
    body = RichTextUploadingField(_('body'), blank=True)
    publish = models.DateTimeField(_('publish'), default=timezone.now)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)
    status = models.CharField(_('status'), max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager(_('tags'))
    watch_total = models.IntegerField(_('watch_total'), default=1)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    def summary(self):
        return self.body[:200]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, max_length=200)
    body = models.TextField(verbose_name='Text')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.post)


class BlockLinks(models.Model):
    title = models.CharField(max_length=150)
    url = models.URLField(blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Link'

    def __str__(self):
        return self.title
