import requests




class check:
	def __init__(self, domain,api_key):
		self.result = []
		self.revip(domain, api_key)


	def revip(self,domain, apikey):
		if apikey != "":
			r = requests.get("https://api.hackertarget.com/reverseiplookup/?q="+domain+"&apikey="+apikey).text
		else:
			r = requests.get("https://api.hackertarget.com/reverseiplookup/?q=" + domain).text
		if "API count exceeded" in r:
			self.result.append('LIMIT ACCESS!')
		else:
			filtering = r.split()
			for data in filtering:
				self.result.append(data)