from django.db import models


# Create your models here.
class Project(models.Model):

    title       = models.CharField(max_length = 150)
    description = models.TextField()
    short_desc = models.TextField(max_length = 45,default = '#')
    tools       = models.TextField()
    git_link    = models.URLField(max_length = 250)
    image_url = models.URLField(default='#')

    

    def __str__(self):
        return self.title