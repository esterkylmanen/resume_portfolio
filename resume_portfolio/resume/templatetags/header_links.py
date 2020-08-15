from django import template

register = template.Library()

@register.inclusion_tag("navigation.html", takes_context=True)
def navigation(context):
    # The links must have the title as the key and the link as the value
    links = {
        'Résumé': "/resume",
        'Portfolio': "/portfolio",
        'Contact': "/contact",
    }
    return {
        'links': links,
        'request': context['request']
    }

