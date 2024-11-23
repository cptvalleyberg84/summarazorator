from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """Admin configuration for the Post model."""
    list_display = (
        'post_title',
        'post_author',
        'post_status',
        'post_created_on',
        'post_updated_at'
    )
    list_filter = ('post_status', 'post_created_on', 'post_author')
    search_fields = ['post_title', 'post_content', 'post_author__username']
    prepopulated_fields = {'post_slug': ('post_title',)}
    summernote_fields = ('post_content',)
    list_per_page = 20
    date_hierarchy = 'post_created_on'
    actions = ['make_published', 'make_draft']

    def make_published(self, request, queryset):
        """Action to mark selected posts as published."""
        queryset.update(post_status=1)
    make_published.short_description = "Mark selected posts as published"

    def make_draft(self, request, queryset):
        """Action to mark selected posts as drafts."""
        queryset.update(post_status=0)
    make_draft.short_description = "Mark selected posts as drafts"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin configuration for the Comment model."""
    list_display = (
        'truncated_comment',
        'comment_author',
        'parent_post',
        'comment_type',
        'comment_created_on',
        'comment_approved'
    )
    list_filter = (
        'comment_created_on',
        'comment_approved',
        'comment_type',
        'comment_author'
    )
    search_fields = [
        'comment_body',
        'comment_author__username',
        'parent_post__post_title'
    ]
    list_per_page = 30
    date_hierarchy = 'comment_created_on'
    actions = ['approve_comments', 'disapprove_comments']

    def truncated_comment(self, obj):
        """Return truncated comment body for list display."""
        return obj.comment_body[:50] + '...' if len(obj.comment_body) > 50 else obj.comment_body
    truncated_comment.short_description = 'Comment'

    def approve_comments(self, request, queryset):
        """Action to approve selected comments."""
        queryset.update(comment_approved=True)
    approve_comments.short_description = "Approve selected comments"

    def disapprove_comments(self, request, queryset):
        """Action to disapprove selected comments."""
        queryset.update(comment_approved=False)
    disapprove_comments.short_description = "Disapprove selected comments"
