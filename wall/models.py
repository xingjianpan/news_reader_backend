from django.db import models

# Create your models here.


class Post(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    owner = models.ForeignKey('users.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)
