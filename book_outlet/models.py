from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)
    
    def __str__(self):
        return f"{self.name}"
        
    class Meta:
        verbose_name_plural = "Countries"

class Address(models.Model):
    street = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"
    
    #to change the name address to address entries in admin
    class Meta: 
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def __str__(self):
        # return f"{self.first_name} {self.last_name}"
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    # author = models.CharField(null=True, max_length=100)
    author = models.ForeignKey("book_outlet.Author", on_delete=models.CASCADE, null=True, related_name="book_set") #verbose_name=_("")
    is_bestselling = models.BooleanField(default=False)
    # slug = models.SlugField(default="", null=False) #harry potter 1 => harry-potter-1
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) #harry potter 1 => harry-potter-1
    #editable=False,
    #db_index=True => makes the field searching quicker
    #I can make the slug to be the primary key primary_key=True
    published_countries = models.ManyToManyField(Country)
    
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
        
        
    def get_absolute_url(self):
        # return reverse("book_detail", args=[self.id])
        return reverse("book-detail", args=[self.slug])
    
    def __str__(self):
        return f"{self.title} ({self.rating})"
