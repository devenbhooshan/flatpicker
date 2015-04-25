import requests
from cons import *

class Maps:
	def __init__(self,url,dis_url):
		self.url=url
		self.dis_url=dis_url

	def find_locations(self,lat,long,city):
		url=self.url.format(lat=lat,long=long)
		response=requests.get(url)
		locations=response.json()['results']
		loc=[]
		latlong=[]
		for location in locations:	
			pl=location['vicinity'].split(",")[:-1]
			# print(location)
			
			origin =str(location['geometry']['location']["lat"]) + "," + str(location['geometry']['location']["lng"])
			destination =lat + "," + long
			dis_response=requests.get(dis_url.format(origin=origin,destination=destination))
			distance=dis_response.json()['rows'][0]['elements'][0]['distance']["text"]
			
			for first in pl:
					try:
						new_loca=first.lower().strip()
						if new_loca and new_loca not in city and  new_loca not in loc:
							
							loc.append([new_loca,distance])
					except:
						pass
		return loc



