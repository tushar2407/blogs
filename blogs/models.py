from django.db import models
from django.template.defaultfilters import slugify
from django.controb.auth.models import User
# Create your models here.
class Blog(models.Model):
    body=models.TextField()
    heading=models.CharField(max_length=1000)
    slug=models.SlugField(max_length=200, unique=True)
    def __str__(self):
        return self.heading
    def save(self,*args,**kwargs):
        if not self.id:
            self.slug=slugify(self.heading)
        super(Blog,self).save(*args,**kwargs)
