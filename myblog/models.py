from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.TextField(max_length=50, default='')
    cover = models.ImageField(upload_to='images/mens/')

    def __str__(self):
        return self.title
