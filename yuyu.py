import requests 
import json
import argparse
import sys
import os
from lib import email
from lib import subdomain
from lib import checkhost
from lib import protocheck
from lib import technologies
from lib import reverseip
from lib import whois
from lib import wayback
from lib import wayback_files
from lib import wayback_document
from lib import wayback_uri
from lib import wayback_js
from lib import securityheaders
from lib import cors
from lib import file
from lib import portscan
from lib import output
from halo import Halo
import time

class Yuyu:
	def __init__(self, targets, args):
		self.opt = args
		self.subdomain = []
		self.protocol = []
		self.livehost = {}
		self.reverseip = []
		self.files = []
		self.whois = ""
		self.scanport = {}
		self.securityheaders = {}
		self.corsmis = []
		self.technologies = []
		self.email = []
		self.wayback = []
		self.wayback_files = []
		self.wayback_uri = []
		self.wayback_document = []
		self.wayback_js = []
		self.timeout = args.timeout
		self.output = args.output

		settings = open("settings.json", "r").read()
		self.api_key = json.loads(settings)

		if len(targets) != 0:
			for target in targets:
				domain = target.replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")
				self.start(domain)



	def start(self, domain):
		# ! Check arguments !

		# check if subdomain and checklive is true
		if  self.opt.subdomainfinder == True and self.opt.checklive == True:

			self.subdomain = subdomain.check(domain).result 
			print("\n\n%s\n-------------------------------" %("Subdomain Finder"))
			for subdo in self.subdomain:
				print("-> %s" % (subdo))
			


			self.livehost = checkhost.check(self.subdomain).result
			print("\n\n%s\n-------------------------------" %("LiveHost"))
			for host in self.livehost:
				print("-> %s [%s]" % (host[0], host[1]))
			
			


			# check opt for livehost
			if self.opt.checkprotocol == True:

				# RUN FUNCTION FOR PROTOCOL http/s IS READY 
				host = [i[0] for i in self.livehost if i[1] != False]
				self.protocol = protocheck.check(host, self.timeout).result
				print("\n\n%s\n-------------------------------" %("Protocol http/s"))
				for host in self.protocol:
					print("-> %s " % (host))
				
				

				if self.opt.checktech == True:
					self.technologies = technologies.check(self.protocol).result
					print("\n\n%s\n-------------------------------" %("Technology"))
					for tech in self.technologies:
						print("-> %s \n\tStatus Code :  %s \n\tTitle : %s \n\tTechnologies : " % (tech[0], str(tech[1]), tech[3]))
						for vendor in tech[2]:
							print("\t\t - %s : %s" % (vendor, tech[2][vendor]['versions']))
					
					

				if self.opt.securityheaders == True:
					self.securityheaders = securityheaders.check(self.protocol).result
					print("\n\n%s\n-------------------------------" %("Missing Security Headers"))
					for sechead in self.securityheaders:
						for sec in sechead:
							print("-> %s " % (sec))
							for val in sechead[sec]:
								print("\t- %s " % (val))

					

				if self.opt.corscheck == True:
					self.corsmis = cors.check(self.protocol).result
					print("\n\n%s\n-------------------------------" %("CORS"))
					if len(self.corsmis) != 0:
						for data in self.corsmis:
							print("-> %s " % (data))
						print(self.corsmis)
					else:
						print("-> No one CORS Found!")
					


				if self.opt.filesensitive == True:
					self.files = file.check(self.protocol, "file_scan.json").result
					print("\n\n%s\n-------------------------------" %("Sensitive File"))
					for data in self.files:
						print("-> %s " % (data))
					

			if self.opt.scanport == True:
				host = [i[1] for i in self.livehost]
				self.scanport = portscan.check(host).result
				print("\n\n%s\n-------------------------------" %("Port Scan"))
				for ip in self.scanport:
					print("-> %s" % (ip[0]))
					for port in ip[1]:
						print("\t- Port %s (%s) is %s" % (port[0], port[1], port[2])) 
				


				# scanport

		else:

			# there is singgle target
			if self.opt.subdomainfinder == True:
				self.subdomain = subdomain.check(domain).result 
				print("\n\n%s\n-------------------------------" %("Subdomain Finder"))
				for subdo in self.subdomain:
					print("-> %s" % (subdo))
			
				

		if self.opt.revip == True:
			self.reverseip = reverseip.check(domain, self.api_key['hackertarget']).result
			print("\n\n%s\n-------------------------------" %("Reverse IP"))
			if "LIMIT ACCESS!" not in self.reverseip:
				print("-> Total Domain Found : %s " % (len(self.reverseip)))
			else:
				print("LIMIT ACCESS!")

		if self.opt.whois == True:
			self.whois = whois.check(domain).result
			print("\n\n%s\n-------------------------------" %("WHOIS"))
			print(self.whois)
			

		if self.opt.collecturl == True:
			self.wayback = wayback.check(domain)
			self.waybackdata = self.wayback.result
			wb_name = self.wayback.tmp_name
			print("\n\n%s\n-------------------------------" %("WaybackURL"))
			print("-> Total Found URL : %s " % (len(self.wayback.result)))
			

			if self.opt.extractfiles == True:
				self.wayback_files = wayback_files.check(wb_name).result
				print("-> Extracted Files : %s " % (len(self.wayback_files)))
				

			if self.opt.extracturi == True:
				self.wayback_uri = wayback_uri.check(wb_name).result
				print("-> Extracted URI's : %s " % (len(self.wayback_uri)))
				

			if self.opt.extractdocument == True:
				self.wayback_document = wayback_document.check(wb_name).result
				print("-> Extracted Document's : %s " % (len(self.wayback_document)))
				

			if self.opt.extractjs == True:
				self.wayback_js = wayback_js.check(wb_name).result
				print("-> Extracted JS Files : %s " % (len(self.wayback_js)))
				

			pwd = os.getcwd()
			join = os.path.join(pwd,wb_name)
			if os.path.isfile(join):
				os.remove(join)				

		if self.opt.emailsearch == True:
			self.email = email.check(domain, self.api_key['hunterio']).result
			print("\n\n%s\n-------------------------------" %("Email Finder"))
			for mail in self.email:
				print("-> %s " % (mail))
			

		if self.opt.output != None:
			if self.opt.subdomainfinder == True:
				output.generate("subdomainfinder", self.opt.output, domain, self.subdomain)
			if self.opt.checklive == True:
				output.generate("checklive", self.opt.output, domain, self.livehost)
			if self.opt.checkprotocol == True:
				output.generate("checkprotocol", self.opt.output, domain, self.protocol)
			if self.opt.checktech == True:
				output.generate("checktech", self.opt.output, domain, self.technologies)
			if self.opt.corscheck == True:
				output.generate("corscheck", self.opt.output, domain, self.corsmis)
			if self.opt.securityheaders == True:
				output.generate("securityheaders", self.opt.output, domain, self.securityheaders)
			if self.opt.revip == True:
				output.generate("revip", self.opt.output, domain, self.reverseip)
			if self.opt.whois == True:
				output.generate("whois", self.opt.output, domain, self.whois)
			if self.opt.collecturl == True:
				output.generate("collecturl", self.opt.output, domain, self.waybackdata)
			if self.opt.extracturi == True:
				output.generate("extracturi", self.opt.output, domain, self.wayback_uri)
			if self.opt.extractjs == True:
				output.generate("extractjs", self.opt.output, domain, self.wayback_js)
			if self.opt.extractfiles == True:
				output.generate("extractfiles", self.opt.output, domain, self.wayback_files)
			if self.opt.extractdocument == True:
				output.generate("extractdocument", self.opt.output, domain, self.wayback_document)
			if self.opt.emailsearch == True:
				output.generate("emailsearch", self.opt.output, domain, self.email)
			if self.opt.scanport == True:
				output.generate("scanport", self.opt.output, domain, self.scanport)
			if self.opt.filesensitive == True:
				output.generate("filesensitive", self.opt.output, domain, self.files)

			# output.generate("subdomain", domain, self.subdomain)

			# s = self.opt.output
			# output.generate(self.output, domain, self.subdomain, self.protocol,
			 # self.livehost, self.reverseip, self.files, self.whois, self.scanport, self.securityheaders, self.corsmis, self.technologies, self.email, self.waybackdata, self.wayback_files, self.wayback_uri, self.wayback_document, self.wayback_js, self.timeout)
		if self.opt.report == True:
			pass





if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('-u', '--url', action='store', help='Target URL')
	parser.add_argument('-f', '--file', action='store', help='Target URL From File')
	parser.add_argument('-g', '--gui', action='store_true', help="Run Yuyu in Gui Mode")
	parser.add_argument('-s', '--subdomainfinder', action='store_true', help="Find Subdomain")
	parser.add_argument('-cl', '--checklive', action='store_true', help="Check LiveHost")
	parser.add_argument('-cp', '--checkprotocol', action='store_true', help="Check protocol http/s")
	parser.add_argument('-ct', '--checktech', action='store_true', help="Check technologies are used")
	parser.add_argument('-cors', '--corscheck', action='store_true', help="Check CORS Misconfiguration")
	parser.add_argument('-sh', '--securityheaders', action='store_true', help="Check Missing Security Headers")
	parser.add_argument('-ri', '--revip', action='store_true', help="Reverse IP from target URL")
	parser.add_argument('-ws', '--whois', action='store_true', help="Whois Lookup from target URL")
	parser.add_argument('-cu', '--collecturl', action='store_true', help="Collect URL from Webarchive / Waybackurl")
	parser.add_argument('-eu', '--extracturi', action='store_true', help="Extract URI from Collected URL From Webarchive / Waybackurl")
	parser.add_argument('-ej', '--extractjs', action='store_true', help="Extract JS Files from Collected URL From Webarchive / Waybackurl")
	parser.add_argument('-ef', '--extractfiles', action='store_true', help="Extract Files from Collected URL From Webarchive / Waybackurl")
	parser.add_argument('-ed', '--extractdocument', action='store_true', help="Extract Document from Collected URL From Webarchive / Waybackurl")
	parser.add_argument('-es', '--emailsearch', action='store_true', help="Find Email Address")
	parser.add_argument('-sp', '--scanport', action='store_true', help="Port Discovery from Discovery IP")
	parser.add_argument('-fs', '--filesensitive', action='store_true', help="Find Sensitive Files from Subdomain Result")
	parser.add_argument('-to', '--timeout',help="Timeout for requests, default : 5", nargs='?', const=1, type=int, default=5)
	parser.add_argument('-o', '--output', action='store', help="Output")
	parser.add_argument('-r', '--report',action='store_true', help="Generate Report")

	args = parser.parse_args()
	if sys.stdin.isatty():
		if args.url:
			Yuyu([args.url],args)
		elif args.file:
			o = [i.strip() for i in open(args.file, "r").readlines()]
			Yuyu(o, args)
	else:
		o = [i.strip() for i in sys.stdin.readlines()]
		Yuyu(o, args)
