# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    headline = models.CharField(max_length=500, blank=True, null=True)
    fly_title = models.CharField(max_length=500, blank=True, null=True)
    alternativename = models.CharField(max_length=500, blank=True, null=True)
    content_dirty = models.TextField(blank=True, null=True)
    content_clean = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=500, blank=True, null=True)
    source = models.CharField(max_length=500, blank=True, null=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    url = models.URLField(max_length=500, editable=False)
    spider = models.CharField(max_length=500, editable=False)
    create_date = models.DateTimeField(editable=False)
    project = models.CharField(max_length=500, editable=False)

    class Meta:
        ordering = ['-source', 'category']

    def __str__(self):              # __unicode__ on Python 2
        return self.headline


    def __unicode__(self):
        return self.headline
