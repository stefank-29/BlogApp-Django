from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # veza sa User modelom (ako se obrise user brise se i profil)
    image = models.ImageField(default='user.svg', upload_to='profile-pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        image = Image.open(self.image.path)
        if image.height > 400 or image.width > 400:
            output_size = (400, 400)
            image.thumbnail(output_size)
            image.save(self.image.path)


