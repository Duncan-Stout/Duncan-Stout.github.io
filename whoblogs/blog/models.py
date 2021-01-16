from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hoot(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    total_likes = models.IntegerField(default=0)
    image = models.CharField(max_length=240, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.title

   



class Comment(models.Model):
    hoot = models.ForeignKey(Hoot, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date= models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.body
