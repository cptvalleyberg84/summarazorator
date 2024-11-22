from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('post_title', 'post_slug', 'post_status', 'post_created_on')
    search_fields = ['post_title', 'post_content']
    list_filter = ('post_status', 'post_created_on',)
    prepopulated_fields = {'post_slug': ('post_title',)}
    summernote_fields = ('post_content',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_body', 'comment_author', 'parent_post', 'comment_created_on')
    list_filter = ('comment_created_on',)
