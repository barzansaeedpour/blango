from django.contrib import admin

# Register your models here.
from blog.models import Tag, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['slug','published_at']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)