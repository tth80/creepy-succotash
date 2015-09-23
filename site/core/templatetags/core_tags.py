from django import template
from markdown import markdown as markdown_func


register = template.Library()


@register.filter
def markdown(value):
    return markdown_func(value, extensions=['markdown.extensions.tables'])
