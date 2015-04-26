import glob, os, csv
import constants

FOLDER_PATH = "/Users/shashank/Dropbox/flatpicker/"


def get_company_details():
	csvFiles = glob.glob(FOLDER_PATH + "*.csv")
	companies = set()
	latlong = []
	for inputFile in csvFiles:
		with open(inputFile, 'rb') as f:
			items = csv.DictReader(f)
			for item in items:
				companies.add(item[constants.KEY_COMPANY_NAME])
				latlong.append(item)

	return companies, latlong

if __name__ == '__main__':
	print get_company_details()
