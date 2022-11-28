from django.contrib import admin
from blog.models import Tag, Post, Comment

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


# class CommentAdmin(admin.ModelAdmin):
#     fields = ('creator','content','content_type')
#     list_display = ('creator','content','content_type')

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)