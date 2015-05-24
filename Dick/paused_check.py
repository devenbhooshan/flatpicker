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
	paused = listingItem.find("span", {"class" : "expired-text"}).text.strip()
	if "paused" in paused.lower():
		flat.approved = False
	flat.save()	

all_flats=Flat.objects.all()
for af in all_flats:
	try:
		get_data(af)
	except:
		print("Flat is not paused")