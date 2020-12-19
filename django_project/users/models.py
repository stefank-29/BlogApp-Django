from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # veza sa User modelom (ako se obrise user brise se i profil)
    image = models.ImageField(default='user.svg', upload_to='profile-pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    


