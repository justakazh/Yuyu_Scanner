import socket
import subprocess
import xml.etree.ElementTree as ET
import string
import random
import os
import socket

class check:
	def __init__(self, lists):
		self.result = []
		self.ip = []
		letters = string.ascii_lowercase
		rand =  ''.join(random.choice(letters) for i in range(10))
		self.name = "ip_"+str(rand)
		for data in lists:
			if data not in self.ip and data != False:
				open(self.name, "a").write(data+"\n")
				self.ip.append(data)
		self.scan()

	def scan(self):
		out = "result_%s" % (self.name)
		cmd = subprocess.getoutput("nmap -Pn -p 21,22,23,25,53,80,110,115,135,139,143,194,443,445,1433,3306,3389,5632,5900,25565 --open -oX %s -iL %s" % (out,self.name))
		res = open(out, "r").read()
		tree = ET.fromstring(res)
		for i in tree.findall('host'):
			data = []
			ip = i.find("address").get("addr")
			for ii in i.findall("ports"):
				for iii in ii.findall('port'):
					port = iii.get("portid")
					service = iii.find("service").get("name")
					ps = port+"/"+service+"|"
					data.append([port, service, "open"])

			self.result.append([ip,data])
		os.remove(self.name)
		os.remove(out)

