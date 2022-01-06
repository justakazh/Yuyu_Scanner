import requests
import re
import socket
from multiprocessing.dummy import Pool
from lib.manage import file
from lib.color import pelangitapibukangay as colors
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class check():
	def __init__(self, hostlist, timeout):
		self.timeout = timeout
		print("\n"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("blue")+"+"+colors.warnaihidupku("white")+"] Checking For CORS Missconfiguration\t")
		print("---------------------------------")
		x = Pool(int(len(hostlist)))
		x.map(self.process, hostlist)
		x.close()
		x.join()

	def process(self, domain):
		try:
			r = requests.get("http://"+domain, timeout=self.timeout, headers={"Origin": "evil-sites.com"})
			header = r.headers
			if "evil-sites.com" in header:
				print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("green")+">"+colors.warnaihidupku("white")+"] "+ domain + " "+colors.warnaihidupku("red")+"["+colors.warnaihidupku("green")+"CORS Vuln (Not OK)"+colors.warnaihidupku("red")+"] ")
				file.save("cors", domain)
			else:
				print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("red")+"-"+colors.warnaihidupku("white")+"] "+ domain + " "+colors.warnaihidupku("red")+"["+colors.warnaihidupku("green")+"Not Vuln"+colors.warnaihidupku("red")+"] ")


		except requests.exceptions.Timeout  as e:
			print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("red")+"-"+colors.warnaihidupku("white")+"] "+ domain + " "+colors.warnaihidupku("red")+colors.warnaihidupku("red")+"["+colors.warnaihidupku("green")+"Request Timeout!"+colors.warnaihidupku("red")+"] ")
		except requests.exceptions.ConnectionError as e:
			print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("red")+"-"+colors.warnaihidupku("white")+"] "+ domain + " "+colors.warnaihidupku("red")+colors.warnaihidupku("red")+"["+colors.warnaihidupku("green")+"Connection Error!"+colors.warnaihidupku("red")+"] ")
		except Exception as e :
			print(e)

