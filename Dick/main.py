from maps import *
from picker import *
from location import latlong
import os,sys
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] ='flatpicker.settings'
from Core.models import *


m=Maps(url)

companies=Company.objects.all().exclude(name__in=['Amazon','Microsoft','Adobe','Misys','Samsung','Musigma'])
for company in companies:
	try:
		print("Starting crawler for " + company.name)
		location=m.find_locations(latlong[company.name]['Bangalore'][0],latlong[company.name]['Bangalore'][1],['bangalore','bangaluru'])
		p=Picker()
		# location =[u'old madras road', u'bennigana halli', u'kasturi nagar', u'cv raman nagar', u'jal vayu towers']
		# location=location[0:1]
		city,created=City.objects.get_or_create(name='Bangalore')
		# company,created=Company.objects.get_or_create(name='Google')
		valid_locations=p.commonfloor(city,location,company)
	except Exception as e:	
		print ("Error: Could not crawl " + company.name + " . Reason : " + str(e))
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

		