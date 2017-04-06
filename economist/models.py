from __future__ import unicode_literals
from django.db import models
from django.urls import reverse


class Article(models.Model):
    headline = models.TextField(blank=True, null=True)
    fly_title = models.TextField(blank=True, null=True)
    alternativename = models.TextField(blank=True, null=True)
    content_dirty = models.TextField(blank=True, null=True)
    content_clean = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    source_url = models.URLField(editable=False)
    spider = models.TextField(editable=False)
    create_date = models.DateTimeField(editable=False, auto_now_add=True)
    project = models.TextField(editable=False)
    owner = models.ForeignKey(
        'users.User', related_name='articles', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    def __unicode__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse('economist:article_detail', args=[str(self.id)])
