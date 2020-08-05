from django.contrib import admin
from .models import blogs,Author,Comment

# admin.site.register(blogs)
# admin.site.register(Author)
# admin.site.register(Comment)

# Register the Admin classes for Book using the decorator
@admin.register(blogs)
class blogsAdmin(admin.ModelAdmin):
    list_display = ['title','author','pub_date']
    list_filter = ['author']

# Register the Admin classes for BookInstance using the decorator
@admin.register(Author) 
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name','date_of_birth']
    list_filter = ['name']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment','comment_date']