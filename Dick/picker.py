from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
from cons import *
import os,sys
import traceback
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] ='flatpicker.settings'
import django
django.setup()
from Core.models import *

class Picker:
	
	def __init__(self):
		self.display = Display(visible=1, size=(1366, 768))
		self.display.start()
		self.driver = webdriver.Chrome()
		self.urls=urls
		self.title=[]
		self.links=[]
		self.price=[]
		self.address=[]
		self.avail=[]
		self.size=[]
		self.posted=[]
		self.bhk=[]
		self.pic=[]
		self.location=[]
		self.furnished=[]
	def housing(self):
		pass
	
	def crawl(self,v_l,company,area,city):
		import time
		time.sleep(4)
		self.driver.find_element_by_xpath("//div[@class='selectize-input items not-full has-options']").click()
		self.driver.find_element_by_xpath(commonfloor_input_xpath).send_keys(v_l[0])
		import time
		time.sleep(4)
		self.driver.find_element_by_xpath(commonfloor_inputfound_xpath).click()
		try:
			while True:
				self.driver.find_element_by_xpath("//div[@class='show-more show-more-main addCft']/span[1]").click()
				import time
				time.sleep(2)
		except:
			pass
		
		import time
		time.sleep(5)
		self.driver.find_element_by_xpath(commonfloor_h1_xpath).click()
		self.links=[i.get_attribute('href') for i in self.driver.find_elements_by_xpath(commonfloor_links_xpath) if "listing" in i.get_attribute('href') ]
		print(len(self.links))
		# self.links=self.links[0:3]
		for link in self.links:
			self.driver.get(link)
			time.sleep(5)
			try:
				title=self.driver.find_element_by_xpath(commonfloor_title_xpath).text
				price=self.driver.find_element_by_xpath(commonfloor_price_xpath).text

				address=self.driver.find_element_by_xpath(commonfloor_address_xpath).text
				address=", ".join(address.split(","))
				avail=self.driver.find_element_by_xpath(commonfloor_avail_xpath).text
				size=self.driver.find_element_by_xpath(commonfloor_area_xpath).text
				bhk=self.driver.find_element_by_xpath(commonfloor_bhk_xpath).text
				location=self.driver.find_element_by_xpath(commonfloor_location_xpath).text
				
				counter=1
				while counter<=11:
					try:
						furnished=self.driver.find_element_by_xpath(commonfloor_furnished_xpath.format(flag=counter)).text
						if "furnished" in str(furnished).lower():
							break
					except:
						pass
					counter+=1	
				
				

				print("Crawling link : " + link)
				
					
				pic=''
				try:
					pic=self.driver.find_element_by_xpath(commonfloor_pic_xpath).get_attribute('src')
				except:
					pic=self.driver.find_element_by_xpath("//img[@class='default-image']").get_attribute('src')
			except Exception as e:
				print("link : "+ link +" Not crawled" + traceback.format_exc())
				continue
			
			self.add_flat(link,pic,title,price,address,avail,size,bhk,location,company,city,furnished,area,v_l[1])

			self.pic.append(pic)	
			self.title.append(title)
			self.price.append(price)
			self.address.append(address)
			self.avail.append(avail)
			self.size.append(size)
			self.bhk.append(bhk)

	def commonfloor(self,city,locations,company,area):
		self.driver.get(urls['Commonfloor'][city.name])
		
		# driver.find_element_by_xpath("//div[@class='pstd-by-wrp filter-chkbox-block']/label[@class='-lbl'][2]").click()
		import time
		time.sleep(4)
		try:
			self.driver.find_element_by_xpath("//div[@class='selectize-input items not-full has-options']").click()
		except:
			print("Error: Location Input Field not found")
			self.close()
			return False
			
		valid_locations=[]

		for locat in locations:
			location=locat[0]
			latlong=locat[1]
			if len(location)<=5:
				continue
			l=location.split(" ")
			aaa=["1","2","3","4","5","6","7","8","9","0"]
			present=False
			for ll in l:
				for a in aaa:
					if a in ll:
						present=True

			if present:
				continue
							
			self.driver.find_element_by_xpath(commonfloor_input_xpath).send_keys(location)
			import time
			time.sleep(4)
			try:
				self.driver.find_element_by_xpath(commonfloor_inputfound_xpath).click()
				valid_locations.append([location,latlong])
			except:
				self.driver.find_element_by_xpath(commonfloor_h1_xpath).click()	
				continue	
				
		# self.driver.find_element_by_xpath("//div[@id='searchHeaderWidget']/h1").click()

		
		for v_l in valid_locations:
			self.driver.get(urls['Commonfloor'][city.name])
			self.crawl(v_l,company,area,city)
		
		self.close()
		return valid_locations
	
	def add_flat(self,link,pic,title,price,address,avail,size,bhk,location,company,city,furnished,area,distance):

		bhk=float(str(bhk).lower().strip("bhk").strip())
		bhk,created=BHK.objects.get_or_create(bhk=bhk)
		location=Location.objects.get_or_create(name=location)[0]
		
		print(str(location) + str(distance))
		if "furnished" in furnished.lower():
			approved=True
		else:
			approved=False
			

		try:
			Flat.objects.create(title=title,url=link,pic_url=pic,price=price,address=address,bhk=bhk,size=size,location=location,furnished=furnished,approved=approved)
		except:
			Flat.objects.get(url=link).delete()
			Flat.objects.create(title=title,url=link,pic_url=pic,price=price,address=address,bhk=bhk,size=size,location=location,furnished=furnished,approved=approved)
		ll=LocationCompanyCity.objects.get_or_create(location=location,city=city,company=company,area=area)[0]
		ll.distance=distance
		ll.save()
			

		
		


	def close(self):
		self.driver.close()
		self.display.stop()		