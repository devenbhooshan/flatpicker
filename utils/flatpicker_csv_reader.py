import glob, os, csv
from utils.constants import *

FOLDER_PATH ='/home/jolo/docs/' 


def get_company_details():
	csvFiles = glob.glob(FOLDER_PATH + "*.csv")
	companies = set()
	latlong = []
	for inputFile in csvFiles:
		with open(inputFile, 'r') as f:
			items = csv.DictReader(f)
			for item in items:
				companies.add(item[KEY_COMPANY_NAME])
				latlong.append(item)

	return companies, latlong

if __name__ == '__main__':
	print(get_company_details())
