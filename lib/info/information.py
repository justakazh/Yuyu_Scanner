import requests
import re
import socket
from multiprocessing.dummy import Pool
from lib.manage import file
from lib.color import pelangitapibukangay as colors
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class checkInfo():
	def __init__(self, hostlist, timeout):
		self.timeout = timeout
		print("\n"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("blue")+"+"+colors.warnaihidupku("white")+"] Collecting Information\t")
		print("---------------------------------")
		x = Pool(int(len(hostlist)))
		x.map(self.process, hostlist)
		x.close()
		x.join()

	def process(self, domain):
		try:
			r = requests.get("http://"+domain, timeout=self.timeout)
			header = r.headers
			text = r.text
			title = "unknown"
			server = "unknown"
			sc = "unknown"
			try:
				sc = r.status_code
				title = re.findall("<title>(.*?)</title>", text)[0]
				server = header['Server']
			except:
				pass
			print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("green")+">"+colors.warnaihidupku("white")+"] "+ domain + " "+colors.warnaihidupku("red")+"["+colors.warnaihidupku("green")+title+colors.warnaihidupku("red")+"] "+colors.warnaihidupku("red")+"["+colors.warnaihidupku("green")+str(sc)+colors.warnaihidupku("red")+"] "+colors.warnaihidupku("red")+"["+colors.warnaihidupku("green")+str(server)+colors.warnaihidupku("red")+"] ")
			file.save("information", domain + " | "+title+" | "+str(sc)+" | "+ server)
		except requests.exceptions.Timeout  as e:
			print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("red")+"-"+colors.warnaihidupku("white")+"] "+ domain + " "+colors.warnaihidupku("red")+colors.warnaihidupku("red")+"["+colors.warnaihidupku("green")+"Request Timeout!"+colors.warnaihidupku("red")+"] ")
			file.save("information", domain + " | Request Timeout")
		except requests.exceptions.ConnectionError as e:
			file.save("information", domain + " | Connection Error")
			print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("red")+"-"+colors.warnaihidupku("white")+"] "+ domain + " "+colors.warnaihidupku("red")+colors.warnaihidupku("red")+"["+colors.warnaihidupku("green")+"Connection Error!"+colors.warnaihidupku("red")+"] ")
		except Exception as e:
			pass
		# print(e)

