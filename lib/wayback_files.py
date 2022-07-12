import urllib.parse
import subprocess
import html
import furl


class check:
	"""docstring for check"""
	def __init__(self, tmp_name):
		self.result = []

		self.extract(tmp_name)

	def extract(self, tmp_name):
		# 
		# 
		# 
		#  REFERENCES : https://github.com/screetsec/Sudomy/blob/master/plugin/exec_extract_params
		# 
		# 
		# interesting files 
		cmd = 'egrep -i "\.json|\.txt|\.yaml|\.toml|\.xml|\.env|\.config|\.tar|\.rar|\.gz|\.log" %s | sort -u' % (tmp_name)
		run_cmd = subprocess.getoutput(cmd).split()
		for i in run_cmd:
			decodedstr = urllib.parse.unquote(i)
			i = html.unescape(decodedstr)

			if "?" in i:
				f = i.split("?")[0]
				if f not in self.result:
					self.result.append(f)
			else:
				if i not in self.result:
					self.result.append(i)
