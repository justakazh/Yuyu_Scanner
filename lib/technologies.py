from Wappalyzer import Wappalyzer, WebPage
from multiprocessing.dummy import Pool
import requests
import re



class check:
	def __init__(self, targets):
		self.result = []
		for i in targets:
			self.scan(i)
	def scan(self,domain):
		try:
			title = ""
			status_code = ""
			try:
				r = requests.get(domain)
				status_code = str(r.status_code)
				title = re.findall("<title>(.*?)</title>", r.text)[0]
			except:
				title = "unknown"
				status_code = "unknown"
			wappalyzer = Wappalyzer.latest()
			webpage = WebPage.new_from_url(domain)
			wp = wappalyzer.analyze_with_versions(webpage)
			# print([domain,wp,title])
			self.result.append([domain, status_code, wp, title])
		except Exception as e:
			# pass
			print(e)