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
		print("\n"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("blue")+"+"+colors.warnaihidupku("white")+"] Checking For Missing Security Headers\t")
		print("---------------------------------")
		x = Pool(int(len(hostlist)))
		x.map(self.process, hostlist)
		x.close()
		x.join()

	def process(self, domain):
		try:
			r = requests.get("http://"+domain, timeout=self.timeout)
			header = r.headers
			secheader = [
				"X-Content-Type-Options",
				"Content-Security-Policy",
				"X-Frame-Options",
				"Referrer-Policy",
				"Permissions-Policy",
				"Strict-Transport-Security"
			]
			tmp = ""
			for sec in secheader:
				if sec in header:
					pass
				else:
					tmp += sec+" | "
			missing = tmp[:-2]
			print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("green")+">"+colors.warnaihidupku("white")+"] "+ domain + " "+colors.warnaihidupku("red")+"["+colors.warnaihidupku("green")+missing+colors.warnaihidupku("red")+"] ")
			file.save("headers", domain +" | "+missing)

		except requests.exceptions.Timeout  as e:
			print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("red")+"-"+colors.warnaihidupku("white")+"] "+ domain + " "+colors.warnaihidupku("red")+colors.warnaihidupku("red")+"["+colors.warnaihidupku("green")+"Request Timeout!"+colors.warnaihidupku("red")+"] ")
		except requests.exceptions.ConnectionError as e:
			print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("red")+"-"+colors.warnaihidupku("white")+"] "+ domain + " "+colors.warnaihidupku("red")+colors.warnaihidupku("red")+"["+colors.warnaihidupku("green")+"Connection Error!"+colors.warnaihidupku("red")+"] ")
		except Exception as e :
			print(e)

