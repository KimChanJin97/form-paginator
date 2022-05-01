from multiprocessing.shared_memory import ShareableList
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=30, default="")
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.contents[:100]

# comment
class Comment(models.Model):
    post=models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    author_name=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at=models.DateTimeField(auto_now_add = True) 

    def approve(self):
        self.save()

    def __str__(self):
        return self.comment_text

