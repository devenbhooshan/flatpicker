from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from Core.models import *
import json
from constants import GLOBALS

class JsonResponse(HttpResponse):
	def __init__(self, content={}, mimetype=None, status=None,
			 content_type='application/json'):
		super(JsonResponse, self).__init__(json.dumps(content), mimetype=mimetype,
										   status=status, content_type=content_type)

def generate_seo_tags(**kwargs):
	description=kwargs['description']
	title=kwargs['title'] + GLOBALS['user_page_title_postfix']
	url=host_name()+kwargs['url']
	image=kwargs['image']
	seo_tags = []

	seo_tags.append(GLOBALS['meta_description'].format(description=description))
	seo_tags.append(GLOBALS['meta_description_facebook'].format(description=description))
	seo_tags.append(GLOBALS['meta_description_twitter'].format(description=description))


	seo_tags.append(GLOBALS['meta_title_facebook'].format(title=title))
	seo_tags.append(GLOBALS['meta_title_twitter'].format(title=title))

	seo_tags.append(GLOBALS['meta_url_facebook'].format(url=url))
	seo_tags.append(GLOBALS['meta_url_twitter'].format(url=url))

	seo_tags.append(GLOBALS['meta_image_facebook'].format(image=image))
	seo_tags.append(GLOBALS['meta_image_twitter'].format(image=image))

	seo_tags.append(GLOBALS['meta_type_facebook'])
	seo_tags.append(GLOBALS['meta_type_twitter'])
	# seo_tags.append('<meta name="google-site-verification" content="e7AduJBVg3kR7HbuptjixvvKSTp55YQpXcA3qszFQfk" />')
	return seo_tags

def home(request):
	companies=Company.objects.all()

	return render(request,'lp.html')

# def fil<p >{{f.location}}</p>ter(request):
# 	return render(request,'filter.html')

def get_flats(request,company,city,area):
	title_all= "Flats nearest to {company} in {city} | Flatpicker"
	title_area= "Flats nearest to {company} in {area}, {city} | Flatpicker"	
	
	
	
	city=get_object_or_404(City,name=city)
	company=get_object_or_404(Company,name=company)
	area=get_object_or_404(Area,name=area)
	
	if area.name =='all':
		title=  title_all.format(company=company.name, city=city.name)  
		h1 = title_all.format(company="<img src='/static/images/"+ company.img +"'>", city=city.name)  
	else:
		title=  title_area.format(company=company.name, city=city.name, area=area.name)  
		h1 = title_area.format(company=company.img, city=city.name, area=area.name)
	
	locations=LocationCompanyCity.objects.values_list('location').filter(city=city,company=company,area=area)

	flats=Flat.objects.filter(location__in=locations)
	total=len(flats)
	return render(request,'flats.html',{'flats':flats ,'title':title,'h1':h1,'total':total})

def flats(request):
	url="/flats/{company}/{city}/{area}/"

	company=request.POST.get('company',False)
	city=request.POST['city']
	area=request.POST['area']
	if company=='Company' or city=='City':
		return HttpResponseRedirect('/')		
	if not area or area=='All' or area=='Area':
		area='all'
	url=url.format(company=company, city=city, area=area)
	return HttpResponseRedirect(url)	
