import requests
from lib.manage import file
from lib.color import pelangitapibukangay as colors
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class check():
	def __init__(self,ip):
		print("\n"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("blue")+"+"+colors.warnaihidupku("white")+"] Reverse IP\t")
		print("---------------------------------")
		self.process(ip)
		ress = file.openner("revip")
		if "API count exceeded" in ress:
			print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("red")+"!"+colors.warnaihidupku("white")+"] IP Limited, Please use proxy or vpn")
		else:
			print("\n\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("red")+"*"+colors.warnaihidupku("white")+"] Total Found : "+colors.warnaihidupku("green")+str(len(ress)))



	def process(self, ip):
		r = requests.get("https://api.hackertarget.com/reverseiplookup/?q="+ip)
		if "API count exceeded" in r.text:
			open("tmp/revip", "a").write("API count exceeded")
		else:
			domain = r.text.split()
			for site in domain:
				result = site.strip()
				file.save("revip", result+"\n")