from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    # slug = models.SlugField(default="", null=False) #harry potter 1 => harry-potter-1
    slug = models.SlugField(default="", null=False, db_index=True) #harry potter 1 => harry-potter-1
    #db_index=True => makes the field searching quicker
    #I can make the slug to be the primary key primary_key=True
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
        
    def get_absolute_url(self):
        # return reverse("book_detail", args=[self.id])
        return reverse("book_detail", args=[self.slug])
    
    def __str__(self):
        return f"{self.title} ({self.rating})"
