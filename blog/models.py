from django.db import models

# Create a blog model
class Blog(models.Model):
    title = models.CharField(max_length = 50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')
