#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# YUYU project
# I'm a bad Coder so dont expect to much :p


from lib.machine import machine
import lib.subfind as subfind
import lib.livehost as livehost
import lib.info.information as information
import lib.rev.ip as revip
import lib.cu.collecturl as collecturl
import lib.ws.whois as whois
import lib.sp.scanport as scanport
import lib.ed.emaildiscover as emaildiscover
import lib.sh.headers as headers
import lib.cc.cors as cors
import argparse
import sys
from lib.manage import file
import lib.fs.sensitive as sensitive
from lib.color import pelangitapibukangay as colors



class Yuyu:

	def __init__(self, method, data, args):
		# make sure file in tmp folder is empty 
		file.clear()
		# set variable
		self.timeout = args.timeout

		#  check user input method 
		if args.url or data:
			if method == "byone":
				self.target = args.url.replace("http://", "").replace("https://", "").replace("/", "").replace("www.", "")
				self._Subdomain_enumeration(self.target)
				self.someargs(self.target, args)
				self._Output(self.target, args)
				file.clear()
			if method == "bylist":
				for target in data:
					self.target = target.replace("http://", "").replace("https://", "").replace("/", "").replace("www.", "")
					self._Subdomain_enumeration(self.target)
					self.someargs(self.target, args)
					self._Output(self.target, args)
					file.clear()

	def someargs(self, target, args):
		if args.checklive:
			subdolist = file.openner("subdomain")
			self._Check_Livehost(subdolist)

			if args.collectinginformation:
				domainlistlive = file.openner("http")
				self._Collecting_Information(domainlistlive, self.timeout)

			if args.filesensitive:
				seed = file.openner("seed")
				domainlistlive = file.openner("http")
				self._File_Sensitive(seed, domainlistlive, self.timeout)

			if args.scanport:
				domainlistlive = file.openner("ip")
				self._Port_Scan(domainlistlive)

			if args.securityheaders:
				domainlistlive = file.openner("http")
				self._Security_Headers(domainlistlive, self.timeout)

			if args.corscheck:
				domainlistlive = file.openner("http")
				self._Cors_Check(domainlistlive, self.timeout)
		

		if args.whois:
			self._Whois(target)

		if args.revip:
			self._Reverse_IP(target)


		if args.collecturl:
			self._Collect_URL(target)

		if args.emaildiscover:
			self._Email_Discovery(target)


	def _Subdomain_enumeration(self, target):
		subfind.find(target)

	def _Check_Livehost(self, data):
		livehost.check(data)

	def _Collecting_Information(self, data, timeout):
		information.checkInfo(data,timeout)

	def _File_Sensitive(self, seed, data, timeout):
		sensitive.check(seed, data, timeout)

	def _Reverse_IP(self, target):
		revip.check(target)

	def _Collect_URL(self, target):
		collecturl.check(target)

	def _Whois(self, target):
		whois.check(target)

	def _Port_Scan(self, target):
		scanport.scan(target)

	def _Email_Discovery(self, target):
		emaildiscover.check(target)

	def _Security_Headers(self, target, timeout):
		headers.check(target, timeout)

	def _Cors_Check(self, target, timeout):
		cors.check(target, timeout)

	def _Output(self, target, args):
		file.output(target,args)





if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('-u', '--url', action='store', help='Target URL')
	parser.add_argument('-f', '--file', action='store', help='Target URL')
	parser.add_argument('-g', '--gui', action='store_true', help="Run Yuyu in Gui Mode")
	parser.add_argument('-cl', '--checklive', action='store_true', help="Check host live or not")
	parser.add_argument('-ci', '--collectinginformation', action='store_true', help="Collecting Information")
	parser.add_argument('-sh', '--securityheaders', action='store_true', help="Check For Missing Security Headers")
	parser.add_argument('-ri', '--revip', action='store_true', help="Reverse IP from target URL")
	parser.add_argument('-ws', '--whois', action='store_true', help="Whois Lookup from target URL")
	parser.add_argument('-cu', '--collecturl', action='store_true', help="Collect URL from WaybackURL")
	parser.add_argument('-ed', '--emaildiscover', action='store_true', help="Email Discovery")
	parser.add_argument('-sp', '--scanport', action='store_true', help="Port Discovery from Discovery IP")
	parser.add_argument('-cc', '--corscheck', action='store_true', help="CORS missconfiguration Check")
	parser.add_argument('-fs', '--filesensitive', action='store_true', help="Find Sensitive Files from Subdomain Result")
	parser.add_argument('-to', '--timeout',help="Timeout for requests, default : 5", nargs='?', const=1, type=int, default=5)
	parser.add_argument('-sl', '--silent', action='store_true', help="Don't print banner")

	args = parser.parse_args()
	try:
		if args.gui:
			sys.exit(1)
		if sys.stdin.isatty():
			if args.url:
				Yuyu("byone", "" ,args)
			elif args.file:
				o = [i.strip() for i in open(args.file, "r").readlines()]
				Yuyu("bylist", o, args)
		else:
			o = [i.strip() for i in sys.stdin.readlines()]
			Yuyu("bylist", o, args)

	except KeyboardInterrupt:
		print("[!] Procces stoped by user!")
		sys.exit(1)
		
