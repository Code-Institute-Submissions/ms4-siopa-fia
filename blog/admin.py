from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'body',
        'body_one',
        'body_two',
        'body_three',
        'author',
        'published_date',
    )


admin.site.register(Blog, BlogAdmin)
