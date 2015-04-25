from maps import *
from picker import *
from location import latlong
import os,sys
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] ='flatpicker.settings'
from Core.models import *


m=Maps(url,dis_url)

rectricted_terms={}
rectricted_terms['Bangalore']=['bangalore','bangaluru']

companies=Company.objects.filter(name='TCS')
for company in companies:
	try:
		
		latlong=LatLong.objects.filter(company=company)
		print("Starting crawler for " + company.name)
		for ll in latlong:
			print("Area :  " + ll.area.name)
			location=m.find_locations(ll.lat,ll.lon,rectricted_terms[ll.city.name])
			
			p=Picker()
			# location=location[0:2]
			# print(location)
			# location=['whitefield']
			valid_locations=p.commonfloor(ll.city,location,company,ll.area)

	except Exception as e:	
		print ("Error: Could not crawl " + company.name + " . Reason : " + traceback.format_exc())
	# if valid_locations:

	# 	print valid_locations
	# 	print p.title
	# 	print p.price
	# 	print p.links
	# 	print p.bhk
	# 	print p.address
	# 	print p.avail
	# 	print p.area
	# 	print p.pic

		