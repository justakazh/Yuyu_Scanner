import os 
import requests
import re
import json
from lib.manage import file
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def data(url):
	try:
		r = requests.get("https://otx.alienvault.com/api/v1/indicators/domain/"+url+"/passive_dns").text
		d = json.loads(r)
		for i in d['passive_dns']:
			file.save("subdomain", i['hostname']+"\n")
	except Exception as e:
		pass
