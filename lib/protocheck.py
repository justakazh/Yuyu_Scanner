import socket
import requests
from multiprocessing.dummy import Pool


class check:
	def __init__(self, host, timeout):
		self.timeout = timeout
		# print("using timeout : %s " % (timeout) )
		self.ua = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 galer Firefox/102.0"}
		self.result = []
		x = Pool(100)
		x.map(self.proto, host)		
		

	def proto(self, host):
		try:
			http = "http://{}".format(host)
			https = "https://{}".format(host)
			try:
				r = requests.get(http, headers=self.ua, timeout=self.timeout)
				if host in r.request.url:
					pecah = r.request.url.split("/")[2]
					if r.request.url not in self.result:
						pecah = r.request.url.split("/")
						real = pecah[0]+"//"+pecah[2]
						self.result.append(real)
			except:
				r = requests.get(https, headers=self.ua, timeout=self.timeout)
				if host in r.request.url:
					pecah = r.request.url.split("/")[2]
					if r.request.url not in self.result:
						pecah = r.request.url.split("/")
						real = pecah[0]+"//"+pecah[2]
						self.result.append(real)


		except Exception as e:
			pass
			# print(e)