from django.contrib import admin
from django.template.defaultfilters import title

from .models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title', )}
    list_display = ('title', 'author', 'category', 'publication_data')