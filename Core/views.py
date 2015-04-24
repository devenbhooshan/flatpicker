from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from Core.models import *
def home(request):
	companies=Company.objects.all()
	
	return render(request,'homepage.html')

def flats(request,city,company):
	title="Flats nearest to " + company + " in " + city + " | Flatpicker"
	city=get_object_or_404(City,name=city)
	company=get_object_or_404(Company,name=company)
	h1="Flats nearest to <img src='/static/images/" + company.img + "'> in " + city.name
	locations=LocationCompanyCity.objects.values_list('location').filter(city=city,company=company)
	flats=Flat.objects.filter(location__in=locations)
	total=len(flats)
	# print flats[0]

	return render(request,'flats.html',{'flats':flats ,'title':title,'h1':h1,'total':total})	


# Create your views here.
