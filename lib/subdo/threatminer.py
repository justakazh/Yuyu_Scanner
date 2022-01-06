import os 
import requests
import re
import json
from lib.manage import file
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def data(url):
	try:
		r = requests.get("https://api.threatminer.org/v2/domain.php?q="+url+"&rt=5").text
		d = json.loads(r)
		for i in d["results"]:
			file.save("subdomain", i+"\n")
	except Exception as e:
		pass
