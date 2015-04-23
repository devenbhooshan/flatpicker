import requests
from cons import *

class Maps:
	def __init__(self,url):
		self.url=url

	def find_locations(self,lat,long,city):
		url=self.url.format(lat=lat,long=long)
		response=requests.get(url)
		locations=response.json()['results']
		loc=[]
		for location in locations:	
			pl=location['vicinity'].split(",")[:-1]
			for first in pl:
					try:
						new_loca=first.lower().strip()
						if new_loca and new_loca not in city and  new_loca not in loc:
							loc.append(new_loca)
					except:
						pass
		return loc



