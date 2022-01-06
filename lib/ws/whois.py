import subprocess as sp 
from lib.manage import file
from lib.color import pelangitapibukangay as colors




class check():
	def __init__(self, domain):
		print("\n"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("blue")+"+"+colors.warnaihidupku("white")+"] whois\t")
		print("---------------------------------")
		self.process(domain)



	def process(self, domain):
		cmd = sp.getoutput("whois "+domain)
		file.save("whois", cmd)
		print(cmd)