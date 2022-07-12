import subprocess



class check:
	def __init__(self, domain):
		self.result = ""
		self.whois(domain)


	def whois(self, domain):
		cmd = subprocess.getoutput("whois "+domain)
		pecah = cmd.split(">>>")[0]
		self.result = pecah