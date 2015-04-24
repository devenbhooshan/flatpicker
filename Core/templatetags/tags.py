from django import template
register=template.Library()
@register.filter
def format(bhk):
	return str(bhk).rstrip("0").rstrip(".")