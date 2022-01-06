import os 
import requests
import re
import json
from lib.manage import file
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def data(url):
	try:
		r = requests.get("https://riddler.io/search/exportcsv?q=pld:"+url).text
		ss = r.split("\n")
		for i in ss:
			s = re.findall(',(.*?),', r)
			file.save("subdomain", s[5]+"\n")
	except Exception as e:
		pass
