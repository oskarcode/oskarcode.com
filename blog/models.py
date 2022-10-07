from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

# this is how the post generated when user created a post
class Post(models.Model): # each class will be table in the database
          title = models.CharField(max_length= 100)
          content = models.TextField()
          date_posted = models.DateTimeField(default=timezone.now)
          author = models.ForeignKey(User, on_delete =models.CASCADE)
          
          def __str__(self):
                  return self.title
        
          def get_absolute_url(self):
                return reverse('post-detail', kwargs={'pk': self.pk})

class Project(models.Model):
          title = models.CharField(max_length = 100)
          description = models.CharField(max_length = 250)
          image = models.ImageField(upload_to = 'portfolio/images/')
          url = models.URLField(blank= True)

          def __str__(self):
                    return self.title

