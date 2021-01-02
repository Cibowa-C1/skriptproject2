from django.db import models


class Post(models.Model):
    content = models.CharField(max_length=64)

    def _str_(self):
        return self.content


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def _str_(self):
        return self.content