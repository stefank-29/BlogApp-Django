from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Blog(models.Model):
    title = models.CharField(max_length=100)   
    image = models.ImageField(default='logo.png' ,upload_to='blog-images', blank=True) 
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # ako se obrise user brisu se njegovi blogovi
    date_posted = models.DateTimeField(default=timezone.now) # datum kad se blog kreirao (moze da se menja za razliku od auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self): # path to blog
        return reverse("blog-detail", kwargs={"pk": self.pk})

    #* dodavanje metode objektu 
    def content_as_list(self):
        return self.content.split('\n')

    def first_30_words(self):
        return " ".join(self.content.split(' ')[:40])
    