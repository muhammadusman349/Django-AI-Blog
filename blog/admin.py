from django.contrib import admin
from .models import BlogPost
# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'youtude_title', 'youtube_link', 'created_at')
    search_fields = ('user', 'youtude_title')
    list_filter = ('user', 'created_at',)


admin.site.register(BlogPost)
