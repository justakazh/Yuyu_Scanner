import requests
import json
from lib.manage import file
from lib.color import pelangitapibukangay as colors
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class check():
	def __init__(self,domain):
		print(colors.warnaihidupku("white")+"\n["+colors.warnaihidupku("blue")+"+"+colors.warnaihidupku("white")+"] Collecting URL\t")
		print("---------------------------------")
		self.process(domain)


	def process(self,domain):
		r = requests.get("http://web.archive.org/cdx/search/cdx?url=*."+domain+"/*&fl=original&collapse=urlkey").text
		file.save("url", r)
		ress = str(len(file.openner("url")))
		print("\n\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("red")+"*"+colors.warnaihidupku("white")+"] Total Found : "+colors.warnaihidupku("green")+ress)