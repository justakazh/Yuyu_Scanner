import os 
import requests
import re
import json
from lib.manage import file
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def data(url):
	try:
		r = requests.get("https://threatcrowd.org/searchApi/v2/domain/report/?domain="+url).text
		d = json.loads(r)
		for i in d['subdomains']:
			file.save("subdomain", i+"\n")
	except Exception as e:
		pass
