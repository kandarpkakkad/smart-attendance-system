from django import template

register = template.Library()


@register.filter(name='join_list')
def join_list(a, b):
    x = list()
    x.append(a)
    x.append(b)
    return x


@register.filter(name='zip')
def zip_lists(a, b):
    return zip(a[0], a[1], b)


@register.filter(name='to_str')
def to_str(value):
    return str(value)

