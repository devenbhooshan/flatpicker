from maps import *
from picker import *
from location import latlong

m=Maps(url)
location=m.find_locations(latlong['google']['bng'][0],latlong['google']['bng'][1],['bangalore','bangaluru'])
p=Picker()
# location =[u'old madras road', u'bennigana halli', u'kasturi nagar', u'cv raman nagar', u'jal vayu towers']
valid_locations=p.commonfloor('bng',location)
if valid_locations:
	print valid_locations
	print p.title
	print p.price
	print p.links
	print p.bhk
	print p.location
	print p.avail
	print p.area
	print p.pic

		