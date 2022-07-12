import requests
import json




class check:
	def __init__(self, domain, api_key):
		self.result = []
		self.emaildiscovery(domain,api_key)


	def emaildiscovery(self,domain, apikey):
		r = requests.get("https://api.hunter.io/v2/domain-search?domain="+domain+"&api_key="+apikey).text
		j = json.loads(r)
		for mail in j['data']['emails']:
			email = mail['value']
			self.result.append(email)