import requests

class CommonfloorResponse(object):
	"""docstring for CommonfloorResponse"""
	def __init__(self, inputText):
		super(CommonfloorResponse, self).__init__()
		self.inputText = inputText
		self.locations = []
		self.flatsHTML = None

	def __str__(self):
		return self.inputText


def searchOnCommonFloor(inputText, city = "Bangalore"):
	response = CommonfloorResponse(inputText)

	# Get filter dropdown list
	payload = {
		'c' : city,
		'item': 'locationbuilderproject',
		'str': inputText
	}
	autoSuggestUrl = "http://www.commonfloor.com/autosuggest.php"
	# Convert unicode response to python list
	autoSuggestResponse = eval(requests.get(autoSuggestUrl, params = payload).text)

	if len(autoSuggestResponse) > 0:
		filterValue = autoSuggestResponse[0].split("|")

		# Use the first result as the source of truth
		prop_name = filterValue[0].strip('~')
		property_location_filter = filterValue[1]

		getLocalitiesUrl = "http://www.commonfloor.com/property-listing/get-locality-count"
		searchPayload = {
			'location_type': 'near_by',
			'search_intent': 'rent',
			'city':city,
			'house_type[]':'Apartment',
			'set_pp': 'false',
			'property_location_filter[]':property_location_filter,
			'prop_name[]':prop_name,
			'show_ungrouped_results':'0'
		}
		getLocalitiesResponse = requests.post(getLocalitiesUrl, data = searchPayload)
		response.locations = eval(getLocalitiesResponse.text)

		getFlatsUrl = "http://www.commonfloor.com/transformers/search-response/index"
		getFlatsResponse = requests.post(getFlatsUrl, data=searchPayload)
		response.flatsHTML = getFlatsResponse.json()["searchResults"]["html"].encode("ascii", "ignore")

	return response

from bs4 import BeautifulSoup

if __name__ == "__main__":
	result=searchOnCommonFloor("Bennigana Halli")
	html_doc=result.flatsHTML
	soup = BeautifulSoup(html_doc)
	links=soup.find_all('a')
	# import pdb;pdb.set_trace()
