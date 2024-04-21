from django.contrib import admin
from blog.models import Category, Comment, Post

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    # Overrides default admin org and splits into groups
    fieldsets = [
        ("Header", {'fields': ["title", "subtitle", "categories"]}),
        ("Content", {'fields': ["body", "notes"]})
    ]

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)


