from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
from cons import *
class Picker:
	
	def __init__(self):
		self.display = Display(visible=1, size=(1366, 768))
		self.display.start()
		self.driver = webdriver.Chrome()
		self.urls=urls
		self.title=[]
		self.links=[]
		self.price=[]
		self.location=[]
		self.avail=[]
		self.area=[]
		self.posted=[]
		self.bhk=[]
		self.pic=[]
	def housing(self):
		pass
	def commonfloor(self,city,locations):
		
		
		
		self.driver.get(urls['commonfloor'][city])
		self.driver.get(urls['commonfloor'][city])
		# driver.find_element_by_xpath("//div[@class='pstd-by-wrp filter-chkbox-block']/label[@class='-lbl'][2]").click()
		import time
		time.sleep(4)
		try:
			self.driver.find_element_by_xpath("//div[@class='selectize-input items not-full has-options']").click()
		except:
			print "Error: Location Input Field not found"
			self.close()
			return False
			
		valid_locations=[]
		for location in locations:
			self.driver.find_element_by_xpath("//*[@id='top-search-box']/div/div[1]/input").send_keys(location)
			import time
			time.sleep(4)
			try:
				self.driver.find_element_by_xpath("//div[@class='optgroup'][1]/div[@class='active']/span[@class='title']/span[@class='name']").click()
				valid_locations.append(location)
			except:
				self.driver.find_element_by_xpath("//div[@id='searchHeaderWidget']/h1").click()	
				continue	
				
		self.driver.find_element_by_xpath("//div[@id='searchHeaderWidget']/h1").click()

		try:
			while True:
				self.driver.find_element_by_xpath("//div[@class='show-more show-more-main addCft']/span[1]").click()
		except:
			pass		

		import time
		time.sleep(5)
		self.driver.find_element_by_xpath("//div[@id='searchHeaderWidget']/h1").click()
		self.links=[i.get_attribute('href') for i in self.driver.find_elements_by_xpath(commonfloor_links_xpath) if "listing" in i.get_attribute('href') ]
		print len(self.links)
		for link in self.links:
			self.driver.get(link)
			time.sleep(5)
			try:
				title=self.driver.find_element_by_xpath(commonfloor_title_xpath).text
				price=self.driver.find_element_by_xpath(commonfloor_price_xpath).text
				location=self.driver.find_element_by_xpath(commonfloor_location_xpath).text
				avail=self.driver.find_element_by_xpath(commonfloor_avail_xpath).text
				area=self.driver.find_element_by_xpath(commonfloor_area_xpath).text
				bhk=self.driver.find_element_by_xpath(commonfloor_bhk_xpath).text
				pic=''
				try:
					pic=self.driver.find_element_by_xpath(commonfloor_pic_xpath).get_attribute('src')
				except:
					pic=self.driver.find_element_by_xpath("//img[@class='default-image']").get_attribute('src')
			except:
				print "link : "+ link +" Not crawled"
				continue
			self.pic.append(pic)	
			self.title.append(title)
			self.price.append(price)
			self.location.append(location)
			self.avail.append(avail)
			self.area.append(area)
			self.bhk.append(bhk)
			self.close(driver)
		return valid_locations
	
	def close(self):
		self.driver.close()
		self.display.stop()		