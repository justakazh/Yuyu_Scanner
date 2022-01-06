import os 
import requests
import re
import json
from lib.manage import file
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def data(url):
	try:
		s = requests.session()
		get_token = s.get("https://dnsdumpster.com/")
		csrftoken = re.findall("csrftoken=(.*?);", get_token.headers['Set-Cookie'])[0]
		token = re.findall('<form role="form" action="." method="post"><input type="hidden" name="csrfmiddlewaretoken" value="(.*?)">', get_token.text)[0]
		data = {
			"csrfmiddlewaretoken":token,
			"targetip":url,
			"user":"free",
		}
		headers={
			"csrftoken": csrftoken,
			"Referer":"https://dnsdumpster.com/"
		}
		r = s.post("https://dnsdumpster.com/", data=data, headers=headers).text
		get_all = re.findall('<a class="external nounderline" data-toggle="modal" href="(.*?)" data-target="#myModal"><span class="glyphicon glyphicon-globe" data-toggle="tooltip" data-placement="top" title="Get HTTP Headers"></span></a>', r)
		for i in get_all:
			filters = i.split("https://api.hackertarget.com/httpheaders/?q=")[1]
			filtersproto = filters.split("/")
			file.save("subdomain", filtersproto[2]+"\n")
	except Exception as e:
		pass
