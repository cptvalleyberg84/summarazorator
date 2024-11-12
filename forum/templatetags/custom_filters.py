from django import template

register = template.Library()

@register.filter(name='filter_positive')
def filter_positive(comments):
    return [comment for comment in comments if comment.comment_type == 'positive']

@register.filter(name='filter_negative')
def filter_negative(comments):
    return [comment for comment in comments if comment.comment_type == 'negative']
