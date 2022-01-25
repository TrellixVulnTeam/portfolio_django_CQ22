from django.contrib import admin
from .models import Resume, Post


'''

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'content', 'author')


'''

admin.site.register(Resume)
admin.site.register(Post)
