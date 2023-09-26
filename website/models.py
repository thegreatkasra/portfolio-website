from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    sender = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  

    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.name



class Post(models.Model):
    pdf = models.FileField(null=True , upload_to='blog/pdf/')
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=255)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.title