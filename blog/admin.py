from django.contrib import admin
from .models import Post, Comment

# Register your models here.
admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_date', 'active')
    list_filter = ('active', 'created_date')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
