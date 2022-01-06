import os 
import requests
import re
import json
from lib.manage import file
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def data(url):
	try:
		r = requests.get("http://index.commoncrawl.org/CC-MAIN-2020-50-index?url=*."+url+"&output=json").text
		get = re.findall('"url": "(.*?)"', r)
		for i in get:
			s = i.split("/")
			file.save("subdomain", s[2]+"\n")
	except Exception as e:
		pass
