from email.mime import image
from email.policy import default
from operator import mod
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# PIL(Programming Imaging Library) from pip install==> external library for Python programming language that adds support for image
# processing capabilities.

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # :::::::Define inorder to reduce to the large size of image:::::::::::
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)  # Changing size
            img.save(self.image.path)
