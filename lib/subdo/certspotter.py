import os 
import requests
import re
import json
from lib.manage import file
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def data(url):
	try:
		r = requests.get("https://api.certspotter.com/v1/issuances?domain="+url+"&include_subdomains=true&expand=dns_names").text
		d = json.loads(r)
		for i in d:
			file.save("subdomain", i['dns_names'][0]+"\n")
	except Exception as e:
		pass
