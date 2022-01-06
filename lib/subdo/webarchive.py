import os 
import requests
import re
from lib.manage import file
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def data(url):
	try:
		r = requests.get("http://web.archive.org/cdx/search/cdx?url=*."+url+"/&output=text&fl=original&collapse=urlkey").text
		gets = re.findall("://(.*?)/", r)
		get = set(gets)
		for i in get:
			open("tmp/subdomain", "a").write()
			file.save(i+"\n")
		open("tmp/url", "a").write(r)
	except Exception as e:
		return e
		pass
