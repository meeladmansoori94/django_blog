from django.contrib import admin
from .models import Post


# This is a "professional" admin setup. We use ModelAdmin to customize the view.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # This controls what fields you see in the list view
    list_display = ("title", "author", "created_at", "updated_at")
    # This auto-fills the 'slug' field based on the 'title' field as you type
    prepopulated_fields = {"slug": ("title",)}
