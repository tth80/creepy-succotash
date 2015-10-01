from django import template
from django.utils.translation import ugettext_lazy as _
from markdown import markdown as markdown_func
from blog.models import Post


register = template.Library()


@register.filter
def markdown(value):
    return markdown_func(value, extensions=['markdown.extensions.tables'])


@register.assignment_tag(takes_context=True)
def get_breadcrumbs(context):
    request_uri = context.request.path_info
    path_parts = [p for p in request_uri.split('/') if len(p) > 0]

    return [{'class': '', 'title': 'Home', 'url': '/'}] + _get_crumbs_for_path(path_parts)

@register.assignment_tag()
def get_featured_blog_posts():
    # TODO: cache
    return Post.objects.all().order_by('-created_at')[:5]

def _get_crumbs_for_path(parts):
    if len(parts) == 0:
        return []

    path = []
    if parts[0] == 'planner':
        path.append({'class':'', 'title': _('Planner'), 'url': '/planner/'})
        if len(parts) > 1:
            pass
        else:
            path.append({'class':'', 'title': _('Index'), 'url': '/planner/'})

    elif parts[0] == 'blog':
        path.append({'class':'', 'title': _('Blog'), 'url': '/blog/'})

        if len(parts) > 1:
            post = Post.objects.get(slug=parts[1])
            path.append({'class':'', 'title': post.title, 'url': post.get_absolute_url()})
        else:
            path.append({'class':'', 'title': _('Index'), 'url': '/planner/'})

    return path
