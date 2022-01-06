import requests
from multiprocessing.dummy import Pool
from lib.manage import file
from lib.color import pelangitapibukangay as colors
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import time

class check():
	def __init__(self, seed, host, timeout):
		self.timeout = timeout
		print("\n"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("blue")+"+"+colors.warnaihidupku("white")+"] Collecting Sensitive File\t")
		print("---------------------------------")
		full = []
		for path in seed:
			for domain in host:
				site = "http://"+domain
				http = site+path
				full.append(http)
		x = Pool(len(full))
		x.map(self.process, full)
		x.close()
		x.join()

		ress = file.openner("file")
		print("\n\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("red")+"*"+colors.warnaihidupku("white")+"] Total Found : "+colors.warnaihidupku("green")+str(len(ress)))



	def process(self, url):
		try:
			r = requests.get(url, verify=False, timeout=self.timeout)
			if "ref: refs/heads/" in r.text:
				print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("red")+">"+colors.warnaihidupku("white")+"] "+url)
				file.save("file", url)
			if "Disallow:" in r.text or "User-agent: *" in r.text or "Allow:" in r.text:
				print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("green")+">"+colors.warnaihidupku("white")+"] "+url)
				file.save("file", url)
			if "XML-RPC server accepts POST requests only." in r.text:
				print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("yellow")+">"+colors.warnaihidupku("white")+"] "+url)
				file.save("file", url)
			time.sleep(3)
		except requests.exceptions.ConnectionError as e:
			pass

		except requests.exceptions.ReadTimeout as e:
			pass

		except:
			pass