from django.db import models

# Create your models here.
import imp
from statistics import mode
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from django.core.files import File
from django import forms

import math
import uuid
import datetime



# Create your models here.
class Cinema(models.Model):
    name = models.CharField(max_length=64, unique=True)
    picture = models.TextField(max_length=512, null=True)
    location = models.CharField(max_length=64,null=True)
    description = models.CharField(max_length=64, null=True)
    book_ticket = models.CharField(max_length=64, null=True)
    review = models.CharField(max_length=64, null=True)
    visit = models.IntegerField()
    slug = models.SlugField(unique=True, null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(str(self))
    #     super(Cinema, self).save(*args, **kwargs)
    
    # class Meta:
    #     verbose_name_plural = 'Categories'

    # def __str__(self):
    #     return str(self.name)

class Category(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural = 'Categories'

        
    def __str__(self):
        return self.name



class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username