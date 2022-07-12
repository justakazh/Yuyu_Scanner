import requests
import json
from multiprocessing.dummy import Pool



class check:
	def __init__(self, targets, paths):
		self.result = []
		target = []
		self.path = json.loads(open(paths, "r").read())
		for domain in targets:
			for i in self.path:
				target.append("%s/%s" % (domain, i))
		x = Pool(100)
		x.map(self.filecheck, target)


	def filecheck(self, target):
		r = requests.get(target).text
		for text in self.path:
			if self.path[text][0] in r:
				self.result.append(target)