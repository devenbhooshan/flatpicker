import os,sys
import traceback
from bs4 import BeautifulSoup

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH2=os.path.abspath(os.path.join(PROJECT_PATH, os.pardir))
sys.path.append(PROJECT_PATH)

os.environ['DJANGO_SETTINGS_MODULE'] ='flatpicker.settings'
import django
django.setup()
from extractlinks import *
from Core.models import *
from utils.flatpicker_csv_reader import get_company_details
import utils.constants as constants

companies, latlong= get_company_details()

all_locations=Location.objects.all()
all_flats=Flat.objects.all()

for al in all_locations:
	al.crawled=False
	al.save()

for af in all_flats:
	af.crawled=False
	af.save()


def store_links(html_doc,location):
	soup = BeautifulSoup(html_doc)
	all_links=[ constants.CF_LINK_PREFIX + i.get('href') for i in soup.find_all('a') if 'listing' in i.get('href') and '-sale-' not in i.get('href') ]

	for url in all_links:
		flat=Flat.objects.get_or_create(url=url)[0]
		flat.location=location
		flat.save()
		



for ll in latlong:
	company_name = ll[constants.KEY_COMPANY_NAME]
	area_name = ll[constants.KEY_LOCALITY]
	city_name = ll[constants.KEY_CITY]
	
	if company_name:
		print("----Crawler started for : "+company_name +'----')
		try:
			print("-----Area :  " + area_name +'----')
			
			company=Company.objects.get_or_create(name=company_name)[0]
			city=City.objects.get_or_create(name=city_name)[0]
			area=Area.objects.get_or_create(name=area_name)[0]
			location=Location.objects.get_or_create(name=area_name)[0]
			LocationCompanyCity.objects.get_or_create(company=company,city=city,area=area,location=location)
			location.crawled = True
			location.save()

			response=searchOnCommonFloor(area_name,city_name)
			near_locations=response.locations
			html_doc=response.flatsHTML

			if html_doc:
				print(location.name)
				try:
					store_links(html_doc,location)
				except:
					print("Error : Not able to add links for the location : " + location + " . Reason : " + traceback.format_exc())
					
			if near_locations:
				for nl in near_locations:
					nl_name=nl['name']	
					new_location=Location.objects.get_or_create(name=nl_name)[0]
					LocationCompanyCity.objects.get_or_create(company=company,city=city,area=area,location=new_location)
					if not new_location.crawled:
						new_location.crawled = True
						new_location.save()
						html_doc=searchOnCommonFloor(nl_name,city_name).flatsHTML
						try:
							store_links(html_doc,new_location)
						except:
							print("Error : Not able to add links for the location : " + new_location + " . Reason : " + traceback.format_exc())
			else:
				print ("No result found for Area : " + area_name)
		except:	
			print ("Error: Could not crawl " + company_name+ " . Reason : " + traceback.format_exc())
	else:
		print ("Empty company name detected")
			
