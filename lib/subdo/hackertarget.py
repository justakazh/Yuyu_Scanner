import os 
import requests
import re
import json
from lib.manage import file
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def data(url):
	try:
		r = requests.get("https://api.hackertarget.com/hostsearch/?q="+url).text
		d = r.split("\n")
		for i in d:
			if "API count exceeded " in i:
				pass
			else:
				filters = i.split(",")
				file.save("subdomain", filters[0]+"\n")
	except Exception as e:
		pass
