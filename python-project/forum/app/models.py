from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True, default=None)
    @property
    def Discussion_count(self):
        return self.discussion_set.count()

    def __str__(self):
        return self.name

class Discussion(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    subject = models.CharField(max_length=1024)
    text = models.TextField(null=False)
    issued = models.DateTimeField(default=datetime.now(), null=False)

    def __str__(self):
        return self.subject[:10]
    
    @property
    def Likes(self): 
        
        return self.likediscussion_set.count()
    @property
    def Comments(self):
        return self.comment_set.count()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.RESTRICT, null=False)
    text = models.TextField(null=False)
    issued = models.DateTimeField(default=datetime.now, null=False)

    discussion = models.ForeignKey(Discussion, on_delete=models.DO_NOTHING, null=False)

    def __str__(self):
        return self.text[:10]
    
    @property
    def Likes(self): 
        
        return self.likecomment_set.count()

class LikeDiscussion(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    discussion = models.ForeignKey(Discussion, on_delete=models.DO_NOTHING)

class LikeComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comment = models.ForeignKey(Comment, on_delete=models.DO_NOTHING)