import os 
import requests
import re
import json
from lib.manage import file
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def data(url):
	try:
		r = requests.get("https://rapiddns.io/subdomain/"+url).text
		get = re.findall('<tr>\n<th scope="row ">(.*?)</th>\n<td>(.*?)</td>\n', r)
		for i in get:
			file.save("subdomain", i[1]+"\n")
	except Exception as e:
		pass
