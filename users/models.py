from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    """Create a profile for a user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        #Will print out username and then profile
        return f'{self.user.username} Profile'
    def save(self, *args, **kwargs):
        """To resize image"""
        super().save(*args, **kwargs) #Inherit Parent class save method
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) #Resizes image
            img.save(self.image.path)
