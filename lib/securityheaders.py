from multiprocessing.dummy import Pool
import requests
import json




class check:
	def __init__(self, urls):
		self.result = []
		self.required = [
			"X-Content-Type-Options",
			"X-XSS-Protection",
			"X-Frame-Options",
			"Content-Security-Policy",
			"Referrer-Policy",
			"Permissions-Policy"

		]
		x = Pool(100)
		x.map(self.securityheader, urls)

	def securityheader(self, host):
		tmp = {
			host : []
		}
		r = requests.get(host)
		for head in self.required:
			if head not in r.headers:
				tmp[host].append(head)
		self.result.append(tmp)