from django.contrib import admin
from blog.models import BlogPost


@admin.register(BlogPost)
class BlogpostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content")
    search_fields = ("title", "content")
    list_filter = ("publication_date",)
