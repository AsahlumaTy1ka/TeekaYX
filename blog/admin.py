from django.contrib import admin
from .models import Post
from markdownx.admin import MarkdownxModelAdmin

class PostAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    search_fields = ('title', 'content')
    list_filter = ('date_posted', 'author')
    ordering = ('-date_posted',)

admin.site.register(Post, PostAdmin)
