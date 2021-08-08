from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    intro = models.TextField(max_length=500, blank=False, null=False,
                             default="Intro")
    body_one = models.TextField(blank=False,
                                null=False, default="Paragraph 1")
    body_two = models.TextField(blank=True, null=True)
    body_three = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
