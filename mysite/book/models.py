from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.
        
class Book(models.Model):   
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    quatity = models.IntegerField(default=10)
    in_stock = models.BooleanField()
    isbn = models.IntegerField()
    rating = models.IntegerField(default=3)
    description = models.CharField(max_length=200)
    numberOfPages = models.IntegerField()
    price = models.IntegerField()  
    authors = models.ManyToManyField('Author')

    def __unicode__(self):
        return self.title    

    def has_published(self):
        return self.pub_date <= timezone.now()

        
class Comment(models.Model): 
    book = models.ForeignKey('Book')  
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User)
    
    def __unicode__(self):
        return '<%s> %s' % (self.book.title, self.text)

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __unicode__(self):
        return self.name
        
