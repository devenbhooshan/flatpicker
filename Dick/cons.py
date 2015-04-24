api_key ="AIzaSyDgMZk-bRxgniNznJ8b3lRV6IGTtB_CVYg"
url= "https://maps.googleapis.com/maps/api/place/search/json?location={lat},{long}&radius=1000&sensor=true&key="+api_key
urls= {'Commonfloor':{ 'Bangalore' : 'http://www.commonfloor.com/apartments-for-rent-in-bangalore/cfct-bangalore' }
}
commonfloor_title_xpath ="//h1[@class='listing-title']"
commonfloor_price_xpath = "//div[@class='col-md-3  col-sm-3 col-xs-3']/span[@class='top-details-bold']"
commonfloor_location_xpath ="//div[@class='listing-address']"
commonfloor_avail_xpath="//div[@class='row'][2]/div[@class='col-md-3 col-sm-4 col-md-offset-1 col-sm-offset-0 col-xs-6 list-add-info'][2]/span[@class='bold']"
commonfloor_area_xpath ="//span[@class='top-details-bold']/span[@class='area-val-full-dtl']"
commonfloor_bhk_xpath ="//div[@class='col-md-2 col-sm-2 col-xs-2 col-xs-offset-1 col-sm-offset-0 col-md-offset-0 ']/span[@class='top-details-bold']"
commonfloor_address_xpath="//span[@class='details-item-value address']"
# commonfloor_posted_xpath="//div[@class='snpt-rght-cont ']/div[@class='pull-left']/p[@class='snpt-pstd-by']"
commonfloor_links_xpath="//div[@class='pull-left']/a"
commonfloor_pic_xpath="//a/div[@class='img-wrap']/img"
commonfloor_furnished_xpath="//div[@class='col-md-6 col-md-offset-0 col-sm-5 col-sm-offset-1 col-xs-5 col-xs-offset-1 pd-left-0'][{flag}]/span[@class='details-item-value']"
# commonfloor_title_xpath=commonfloor_title_xpath[0]
# commonfloor_price_xpath=commonfloor_price_xpath[0]
# commonfloor_location_xpath=commonfloor_location_xpath[0]
# commonfloor_avail_xpath=commonfloor_avail_xpath[0]
# commonfloor_area_xpath 
# commonfloor_posted_xpath
