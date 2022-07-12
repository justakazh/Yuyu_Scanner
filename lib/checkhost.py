import socket
from multiprocessing.dummy import Pool


class check:
	def __init__(self, subdomain):
		self.result = []
		self.live = []
		x = Pool(100)
		x.map(self.status, subdomain)		
		

	def status(self, domain):
		try:
			ip = socket.gethostbyname(domain)
			self.result.append([domain,ip])
			self.live.append(domain)
		except:
			self.result.append([domain,False])
			pass