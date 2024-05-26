from django.db import models

# Create your models here.

class Blog(models.Model):
    id = models.BigAutoField(primary_key= True)
    title = models.CharField(max_length = 50)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title