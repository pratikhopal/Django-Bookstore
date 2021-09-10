from books.views import review
from django.contrib import admin
from books.models import book,Review

# Register your models here.
admin.site.register(book)
admin.site.register( Review)