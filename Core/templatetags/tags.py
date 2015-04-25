from django import template
from Core.models import *
register=template.Library()
@register.filter
def format(bhk):
	return str(bhk).rstrip("0").rstrip(".")
@register.filter
def find_distance(cic,l):
	city=cic[0]
	company=cic[1]
	location=l
	return LocationCompanyCity.objects.get(location=location,city=city,company=company).distance
	
