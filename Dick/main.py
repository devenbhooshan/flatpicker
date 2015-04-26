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


for ll in latlong:
	company = ll[constants.KEY_COMPANY_NAME]
	try:
		print("Area :  " + ll[constants.KEY_LOCALITY])
		location=m.find_locations(ll[constants.KEY_LATITUDE],
			ll[constants.KEY_LONGITUDE],
			rectricted_terms[ll[constants.KEY_CITY]])
		
		p=Picker()
		valid_locations=p.commonfloor(ll[constants.KEY_CITY],
			location,
			company,
			ll[constants.KEY_LOCALITY])
	except Exception as e:	
		print ("Error: Could not crawl " + company + " . Reason : " + traceback.format_exc())