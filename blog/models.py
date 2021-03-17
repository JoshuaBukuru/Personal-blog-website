from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Posts(models.Model):
    """data"""
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #when user is deleted posts are deleted

    def __str__(self):#magic
        return self.title

    def get_absolute_url(self):
    	return reverse('blog-home')#kwargs={'pk': self.pk}




