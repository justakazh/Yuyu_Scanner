import requests
import json
import subprocess
import re
import urllib.parse
import html
import furl
import os
from multiprocessing.dummy import Pool

class check:
	def __init__(self, domain):
		self.tmp_name = "tmp_%s.raw" % (domain)
		self.result = []
		self.wayback(domain)
		# self.extract()
		# print(len(self.js),len(self.document),len(self.files))
		# x = Pool(100)
		# x.map(self.extract, self.result)


	def wayback(self,domain):
		url = "http://web.archive.org/cdx/search/cdx?url=*.%s/*&output=text&fl=original&collapse=urlkey" % (domain)
		r = requests.get(url).text
		open(self.tmp_name, "w").write(r)
		self.result = r.split()
		



	# def extract(self):



	# 	# document files
	# 	cmd = 'egrep -i "\.pdf|\.doc|\.docx|\.pptx|\.docm|\.xls|\.xlsx|\.xlsm|\.xps|\.pub" wayback.raw | sort -u'
	# 	run_cmd = subprocess.getoutput(cmd).split()
	# 	for i in run_cmd:
	# 		decodedstr = urllib.parse.unquote(i)
	# 		i = html.unescape(decodedstr)

	# 		if "?" in i:
	# 			f = i.split("?")[0]
	# 			if f not in self.document:
	# 				self.document.append(f)
	# 		else:
	# 			if i not in self.document:
	# 				self.document.append(i)

	# 	# JS files
	# 	cmd = 'egrep -i "\.js" wayback.raw | sort -u'
	# 	run_cmd = subprocess.getoutput(cmd).split()
	# 	for i in run_cmd:
	# 		decodedstr = urllib.parse.unquote(i)
	# 		i = html.unescape(decodedstr)

	# 		if "?" in i:
	# 			f = i.split("?")[0]
	# 			if f not in self.js:
	# 				self.js.append(f)
	# 		else:
	# 			if i not in self.js:
	# 				self.js.append(i)


	# 	# Like gettting admin,api,backup, internal ticket and etc
	# 	cmd = 'cat wayback.raw | egrep -i "/(admin/|api|auth|access|account|beta|board|bin|backup|cgi|create|checkout|debug|dashboard|deploy|get|post|prod|pay|git|purchase|panel|rest|user|member|internal|ticket|test|staging|system|setting|server|java|subscription|private|log|v[0-9]|[1-9]\.[0-9])/" | egrep -v "/wp-(json|content)/"'
	# 	run_cmd = subprocess.getoutput(cmd).split()
	# 	for i in run_cmd:
	# 		decodedstr = urllib.parse.unquote(i)
	# 		i = html.unescape(decodedstr)

	# 		if "?" in i:
	# 			f = i.split("?")[0]
	# 			if f not in self.uri:
	# 				self.uri.append(f)
	# 		else:
	# 			if i not in self.uri:
	# 				self.uri.append(i)








