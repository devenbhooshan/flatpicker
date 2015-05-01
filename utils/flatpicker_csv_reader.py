import glob, os, csv
from utils.constants import *
import os,sys
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH2=os.path.abspath(os.path.join(PROJECT_PATH, os.pardir))
sys.path.append(PROJECT_PATH)

FOLDER_PATH =PROJECT_PATH2 + '/docs/' 


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
