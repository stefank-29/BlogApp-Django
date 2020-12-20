from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=100)    
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # ako se obrise user brisu se njegovi blogovi
    date_posted = models.DateTimeField(default=timezone.now) # datum kad se blog kreirao (moze da se menja za razliku od auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self): # path to blog
        return reverse("blog-detail", kwargs={"pk": self.pk})
    
    
    