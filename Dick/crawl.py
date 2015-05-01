import os,sys
import traceback
from bs4 import BeautifulSoup
import requests
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH2=os.path.abspath(os.path.join(PROJECT_PATH, os.pardir))
sys.path.append(PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] ='flatpicker.settings'
import django
django.setup()
import traceback
from Core.models import *

def get_data(flat):
	url=flat.url
	print("Url: " + url)
	response = (requests.get(url)).text
	soup = BeautifulSoup(response)
	listingItem = soup.find("div", {"class" : "row listing-details"})
	title = listingItem.find("h1", {"class" : "listing-title"}).text.strip()
	top_details=listingItem.findAll("span", {"class" : "top-details-bold"})
	details_key=listingItem.findAll("span", {"class" : "details-item-key"})
	details_value=listingItem.findAll("span", {"class" : "details-item-value"})	# print(top_details)
	pic_tag=listingItem.find("img", {"class" : "flex-lazyload"})

	if pic_tag:
		pic_url=pic_tag['flex-ll-src']
	else:
		pic_url=listingItem.find("img", {"class" : "default-image"})['src']
		
	address=listingItem.find("span", {"class" : "details-item-value address"}).text.strip()
	address=", ".join(address.split(","))
	furnished=''
	for counter,dt in enumerate(details_key):
		if "Furnishing" in dt.text.strip():
			furnished=details_value[counter].text.strip()
			break
		# print(dt.text.strip()+ " : "+details_value[counter].text.strip())
		# print(details_value[counter])
	
	bhk=top_details[0].text
	bhk=str(bhk).lower().strip("bhk").strip()
	price=top_details[1].text
	price=" ".join(price.split(" ")[1:])
	size=top_details[2].text
	flat.title=title
	flat.bhk=bhk
	flat.price=price
	flat.size=size
	flat.address=address
	flat.furnished=furnished
	flat.pic_url=pic_url
	
	# print(bhk)
	# print(size)
	# print(address)
	# print(furnished)

	if "furnished" in furnished.lower():
		flat.approved=True
	else:
		flat.approved=False

	flat.crawled=True
	flat.save()
all_flats=Flat.objects.filter(crawled=False)
for af in all_flats:
	try:
		get_data(af)
	except:
		print("Error : Could not crawl url : " + af.url + " Reason: "+ traceback.format_exc())
		

