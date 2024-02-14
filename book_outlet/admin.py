from django.contrib import admin

from .models import Book, Author, Address

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter  = ("author", "rating",)
    list_display = ("title", "author", )

# class Author(admin.ModelAdmin):
#     list_display = ("first_name", "last_name")
    
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)