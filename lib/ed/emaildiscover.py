import requests
from lib.manage import file
import json
from lib.color import pelangitapibukangay as colors
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



class check():
	def __init__(self, domain):
		print("\n"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("blue")+"+"+colors.warnaihidupku("white")+"] Collecting E-mail\t")
		print("---------------------------------")
		self.process(domain)


	def process(self,domain):
		try:
			mail = []
			hunter_io = "b669c6dbe6b16ef7cda65fa1671fdc1cf7f14705" 
			r = requests.get("https://api.hunter.io/v2/domain-search?domain="+domain+"&api_key="+hunter_io)
			de = json.loads(r.text)
			for email in de['data']["emails"]:
				if email['value'] not in mail:
					mail.append(email['value'])
			for i in mail:
				file.save("mail", i)
				print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("green")+">"+colors.warnaihidupku("white")+"] "+i)
			print("\n\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("red")+"*"+colors.warnaihidupku("white")+"] Total Found : "+colors.warnaihidupku("green")+str(len(mail)))
		except:
			pass