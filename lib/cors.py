from multiprocessing.dummy import Pool
import requests
import json




class check:
	def __init__(self, urls):
		self.result = []
		x = Pool(100)
		x.map(self.cors, urls)

	def cors(self, host):
		r = requests.get(host, headers={
			"Origin": "evil.com"
			}).headers

		if "Access-Control-Allow-Origin: evil.com" in str(r) and "Access-Control-Allow-Credentials: true" in str(r):
			self.result.append(host)
		