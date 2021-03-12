from django.db import models
from django.contrib.auth.models import User

from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_img')
    punkty = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile'






