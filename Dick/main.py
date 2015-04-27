from maps import *
from picker import *
from location import latlong
import os,sys
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] ='flatpicker.settings'
from Core.models import *
from utils.flatpicker_csv_reader import get_company_details
import utils.constants as constants


m=Maps(url,dis_url)

rectricted_terms={}
rectricted_terms['Bangalore']=['bangalore','bengaluru']

companies, latlong= get_company_details()
print(latlong)

for ll in latlong:
	company = ll[constants.KEY_COMPANY_NAME]
	print("Crawler started for : "+company)
	try:
		print("Area :  " + ll[constants.KEY_LOCALITY])
		location=m.find_locations(ll[constants.KEY_LATITUDE],
			ll[constants.KEY_LONGITUDE],
			rectricted_terms[ll[constants.KEY_CITY]])
		print("All Locations:" + str(location) +  " : " +str(len(location)))
		company=Company.objects.get_or_create(name=company)[0]
		city=City.objects.get_or_create(name=ll[constants.KEY_CITY])[0]
		area=Area.objects.get_or_create(name=ll[constants.KEY_LOCALITY])[0]
		p=Picker()
		location=location[2:5]
		valid_locations=p.commonfloor(city,
			location,
			company,
			area)
	except Exception as e:	
		print ("Error: Could not crawl " + company.name+ " . Reason : " + traceback.format_exc())
