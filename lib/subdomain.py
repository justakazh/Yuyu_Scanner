import requests
import sys
import json
import re
import threading
import os
import warnings
warnings.filterwarnings("ignore")
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



class check:
	def __init__(self, target):
		self.subdomain = []
		self.result = []
		self.timeout = 5
		self.ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
		target = target.replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "").strip()
		self._findSubdomain(target)

		asw = []
		liss = [i.strip() for i in self.subdomain]
		for i in liss:
			if target not in i:
				pass
			else:
				asw.append(i)
		subdomain = list(dict.fromkeys(asw))
		self.subdomain.clear()
		for subdo in subdomain: 
			if subdo != "" and "*." not in subdo and ":" not in subdo and "\n" not in subdo and "\r" not in subdo and "@" not in subdo and "?" not in subdo :
				self.result.append(subdo)



	def _findSubdomain(self, target):
		th = [
			threading.Thread(target=self.alienvault, args=(target,)),
			threading.Thread(target=self.certspotter, args=(target,)),
			threading.Thread(target=self.commoncrawl, args=(target,)),
			threading.Thread(target=self.crt, args=(target,)),
			threading.Thread(target=self.dnsdumpster, args=(target,)),
			threading.Thread(target=self.hackertarget, args=(target,)),
			threading.Thread(target=self.rapiddns, args=(target,)),
			threading.Thread(target=self.riddler, args=(target,)),
			threading.Thread(target=self.threatminer, args=(target,)),
			threading.Thread(target=self.threatcrowd, args=(target,)),
			threading.Thread(target=self.urlscan, args=(target,)),
			threading.Thread(target=self.omnisint, args=(target,)),
		]
		for i in th:
			i.start()
		for i in th:
			i.join()


	def alienvault(self, domain):
		try:
			# print("alienvault")
			s = requests.session()
			r = s.get("https://otx.alienvault.com/api/v1/indicators/domain/"+domain+"/passive_dns", timeout=self.timeout, headers={"User-Agent": self.ua}).text
			d = json.loads(r)
			for i in d['passive_dns']:
				self.subdomain.append(i['hostname'])
		except Exception as e:
			# print( e)
			pass

	def certspotter(self, domain):
		try:
			# print("certspotter")
			s = requests.session()
			r = s.get("https://api.certspotter.com/v1/issuances?domain="+domain+"&include_subdomains=true&expand=dns_names", timeout=self.timeout, headers={"User-Agent": self.ua}).text
			d = json.loads(r)
			for i in d:
				self.subdomain.append(i['dns_names'][0])
		except Exception as e:
			# print( e)
			pass

	def commoncrawl(self, domain):
		try:
			# print("commoncrawl")
			s = requests.session()
			r = s.get("http://index.commoncrawl.org/CC-MAIN-2020-50-index?url=*."+domain+"&output=json", timeout=self.timeout, headers={"User-Agent": self.ua}).text
			get = re.findall('"url": "(.*?)"', r)
			for i in get:
				s = i.split("/")
				self.subdomain.append(s[2])
		except Exception as e:
			# print( e)
			pass

	def crt(self, domain):
		try:
			# print("crt")
			s = requests.session()
			r = s.get("https://crt.sh/?q="+domain+"&output=json", timeout=self.timeout, headers={"User-Agent": self.ua}).text
			d = json.loads(r)
			for i in d:
				self.subdomain.append(i['name_value'])
		except Exception as e:
			# print( e)
			pass

	def dnsdumpster(self, domain):
		try:
			# print("dnsdumpster")
			s = requests.session()
			get_token = s.get("https://dnsdumpster.com/")
			csrftoken = re.findall("csrftoken=(.*?);", get_token.headers['Set-Cookie'])[0]
			token = re.findall('<form role="form" action="." method="post"><input type="hidden" name="csrfmiddlewaretoken" value="(.*?)">', get_token.text)[0]
			data = {
				"csrfmiddlewaretoken":token,
				"targetip":domain,
				"user":"free",
			}
			headers={
				"csrftoken": csrftoken,
				"Referer":"https://dnsdumpster.com/"
			}
			r = s.post("https://dnsdumpster.com/", data=data, headers=headers, timeout=self.timeout).text
			get_all = re.findall('<a class="external nounderline" data-toggle="modal" href="(.*?)" data-target="#myModal"><span class="glyphicon glyphicon-globe" data-toggle="tooltip" data-placement="top" title="Get HTTP Headers"></span></a>', r)
			for i in get_all:
				filters = i.split("https://api.hackertarget.com/httpheaders/?q=")[1]
				filtersproto = filters.split("/")
				self.subdomain.append(filtersproto[2])
		except Exception as e:
			# print( e)
			pass

	def hackertarget(self, domain):
		try:
			# print("hackertarget")
			s = requests.session()
			r = s.get("https://api.hackertarget.com/hostsearch/?q="+domain, timeout=self.timeout, headers={"User-Agent": self.ua}).text
			d = r.split("\n")
			for i in d:
				if "API count exceeded " in i:
					pass
				else:
					filters = i.split(",")
					self.subdomain.append(filters[0])
		except Exception as e:
			# print( e)
			pass

	def rapiddns(self, domain):
		try:
			# print("rapiddns")
			s = requests.session()
			r = s.get("https://rapiddns.io/subdomain/"+domain, timeout=self.timeout, headers={"User-Agent": self.ua}).text
			get = re.findall('<tr>\n<th scope="row ">(.*?)</th>\n<td>(.*?)</td>\n', r)
			for i in get:
				self.subdomain.append(i[1])
		except Exception as e:
			# print( e)
			pass

	def riddler(self, domain):
		try:
			# print("riddler")
			s = requests.session()
			r = s.get("https://riddler.io/search/exportcsv?q=pld:"+domain, timeout=self.timeout, headers={"User-Agent": self.ua}).text
			ss = r.split("\n")
			for i in ss:
				s = re.findall(',(.*?),', r)
				self.subdomain.append(s[5])
		except Exception as e:
			# print( e)
			pass

	def threatminer(self, domain):
		try:
			# print("threatminer")
			s = requests.session()
			r = s.get("https://api.threatminer.org/v2/domain.php?q="+domain+"&rt=5", timeout=self.timeout, headers={"User-Agent": self.ua}).text
			d = json.loads(r)
			for i in d:
				self.subdomain.append(i['name_value'])
		except Exception as e:
			# print( e)
			pass

	def threatcrowd(self, domain):
		try:
			# print("threatcrowd")
			s = requests.session()
			r = s.get("https://threatcrowd.org/searchApi/v2/domain/report/?domain="+domain, timeout=self.timeout, headers={"User-Agent": self.ua}).text
			d = json.loads(r)
			for i in d['subdomains']:
				self.subdomain.append(i)
		except Exception as e:
			# print( e)
			pass

	def urlscan(self, domain):
		try:
			# print("urlscan")
			s = requests.session()
			r = s.get("https://urlscan.io/api/v1/search/?q="+domain, timeout=self.timeout, headers={"User-Agent": self.ua}).text
			d = json.loads(r)
			for i in d['results']:
				self.subdomain.append(i['task']['domain'])
		except Exception as e:
			# print( e)
			pass
	def omnisint(self, domain):
		try:
			# print("urlscan")
			s = requests.session()
			r = s.get("https://sonar.omnisint.io/subdomains/"+domain, timeout=self.timeout, headers={"User-Agent": self.ua}).text
			d = json.loads(r)
			for i in d:
				self.subdomain.append(i)
		except Exception as e:
			# print( e)
			pass
