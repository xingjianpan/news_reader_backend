from __future__ import unicode_literals
from django.db import models
from django.urls import reverse


class Article(models.Model):
    headline = models.CharField(max_length=500, blank=True, null=True)
    fly_title = models.CharField(max_length=500, blank=True, null=True)
    alternativename = models.CharField(max_length=500, blank=True, null=True)
    content_dirty = models.TextField(blank=True, null=True)
    content_clean = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=500, blank=True, null=True)
    source = models.CharField(max_length=500, blank=True, null=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    source_url = models.URLField(max_length=500, editable=False)
    spider = models.CharField(max_length=500, editable=False)
    create_date = models.DateTimeField(editable=False, auto_now_add=True)
    project = models.CharField(max_length=500, editable=False)
    owner = models.ForeignKey(
        'users.User', related_name='articles', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-source', 'category']

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    def __unicode__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse('economist:article_detail', args=[str(self.id)])
