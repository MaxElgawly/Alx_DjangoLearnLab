from django.contrib import admin
from.models import Book

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'publication_year', 'author')
    list_display = ('title', 'author', 'publication_year')
    
admin.site.register(Book, BookAdmin)
# Register your models here.
