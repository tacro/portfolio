from django.db import models

# Create a blog model
class Blog(models.Model):
    title = models.CharField(max_length = 30)
    pub_date = models.DateTimeField()
    body = models.CharField(max_length = 500)
    image = models.ImageField(upload_to = 'images/')
