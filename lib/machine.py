import os 
import datetime
from shutil import copyfile
import threading
from lib import subfind
from lib import livehost
from lib.info import information
from lib.manage import file
from lib.rev import ip
from lib.ws import whois
from lib.sp import scanport
from lib.cu import collecturl
from lib.ed import emaildiscover
from lib.fs import sensitive
from lib.http import httpcheck
from multiprocessing.dummy import Pool
from lib.color import pelangitapibukangay as colors

class machine:
	def __init__(self, types, data_target, arg):
		self.result_data = {} 
		self.current_dir =  os.getcwd()
		self.karepmu = arg
		self.pwd = os.getcwd()
		self.date = str(datetime.datetime.now().date())
		self.clear()
		
		if self.karepmu.silent != True:
			self.banner()

		if types == "byone":
			self.target = data_target.replace("http://", "").replace("https://", "").replace("/", "").replace("www.", "") #filter input
			self.process(data_target)
			self.output(data_target)
			self.clear()

		if types == "bylist":
			for asu in data_target:
				self.target = asu.replace("http://", "").replace("https://", "").replace("/", "").replace("www.", "")
				self.process(self.target)
				self.output(self.target)
				self.clear()


		



	def banner(self):
		print("""
                                             
                                      `      
   `-:                                .+.    
  `oo`:.                            `/.-y:   
  :ys+y+`        -/`     -/`       `/yssyo   
  -yyyyys`       -s..:/:`-s`       :yyyyy+   
   +yyyys:-``.-:+syyyyyyyyys+:-.`-/oyyyy+`   
    -+syyyys/yyyyyyyyyyyyyyyyyyy:yyyys/.     
      `+yyyo:yyyyyyyyyyyyyyyyyyy-yyy+.       
        .://:yyyyyyyyyyyyyyyyyyy.-.`         
            .yyyyyyyyyyyyyyyyyyy.             
         `.--+yyyyyyyyyyyyyyyyy:--.`         
     `:+o+/:-`oyyyyyyyyyyyyyyy/`::/oo+-      
     `-`   -/+.+yyyyyyyyyyyyy::+:.  `.-      
         `+o-` -/oyyyyyyyyyo:` `/s-          
         .s.  .y/ ./oyhs+:``s+   /o`         
              `o+     `    .s:    `          
               ``          `.                
                                             
			""")


	
	def process(self, target):
		subfind.find(target) # find subdomain
		self.Checkhost()

		self.Collectinfo() #check host



		if self.karepmu.whois:
			whois.check(target)
			
		if self.karepmu.revip:
			ip.check(target)

		if self.karepmu.collecturl:
			collecturl.check(target)

		if self.karepmu.emaildiscover:
			emaildiscover.check(target)

		if self.karepmu.filesensitive:
			seed = file.openner("seed")
			host = file.openner("hostlive")
			sensitive.check(seed,host)

		if self.karepmu.scanport:
			scanport.scan(target)



	def Checkhost(self):
		host = file.openner("subdomain")
		livehost.check(host)

	def CheckHttp(self):
		host = file.openner("hostlive")
		httpcheck.check(host)

	def Collectinfo(self):
		host = file.openner("hostlive")
		information.checkInfo(host) 

	def clear(self):
		open("tmp/check", "w")
		open("tmp/hostdie", "w")
		open("tmp/hostlive", "w")
		open("tmp/ip", "w")
		open("tmp/mail", "w")
		open("tmp/port", "w")
		open("tmp/revip", "w")
		open("tmp/subdomain", "w")
		open("tmp/url", "w")
		open("tmp/whois", "w")
		open("tmp/ip", "w")
		open("tmp/file", "w")
		open("tmp/information", "w")
		open("tmp/http", "w")


	def output(self, target):
		print("\n"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("blue")+"+"+colors.warnaihidupku("white")+"] Output Result\t")
		print("---------------------------------")
		self.dir = os.path.join(self.pwd, "output/"+self.date+"/"+target)
		try:
			os.makedirs(self.dir)
		except:
			pass

		copyfile("tmp/subdomain", os.path.join(self.dir, "Subdomain.txt"))
		print(""+colors.warnaihidupku("red")+"\t|\n\t|___"+colors.warnaihidupku("white")+"Subdomain\n\t\t"+colors.warnaihidupku("red")+"|__"+colors.warnaihidupku("green")+""+os.path.join(self.dir, "Subdomain.txt"))
		copyfile("tmp/information", os.path.join(self.dir, "Information.txt"))
		print(""+colors.warnaihidupku("red")+"\t|\n\t|___"+colors.warnaihidupku("white")+"Information\n\t\t"+colors.warnaihidupku("red")+"|__"+colors.warnaihidupku("green")+""+os.path.join(self.dir, "Information.txt"))
		if self.karepmu.whois:
			copyfile("tmp/whois", os.path.join(self.dir, "Whois.txt"))
			print(""+colors.warnaihidupku("red")+"\t|\n\t|___"+colors.warnaihidupku("white")+"Whois\n\t\t"+colors.warnaihidupku("red")+"|__"+colors.warnaihidupku("green")+""+os.path.join(self.dir, "Whois.txt"))
			
		if self.karepmu.revip:
			copyfile("tmp/revip", os.path.join(self.dir, "ReverseIP.txt"))
			print(""+colors.warnaihidupku("red")+"\t|\n\t|___"+colors.warnaihidupku("white")+"Reverse IP\n\t\t"+colors.warnaihidupku("red")+"|__"+colors.warnaihidupku("green")+""+os.path.join(self.dir, "ReverseIP.txt"))

		if self.karepmu.collecturl:
			copyfile("tmp/url", os.path.join(self.dir, "CollectedURL.txt"))
			print(""+colors.warnaihidupku("red")+"\t|\n\t|___"+colors.warnaihidupku("white")+"Collected URL\n\t\t"+colors.warnaihidupku("red")+"|__"+colors.warnaihidupku("green")+""+os.path.join(self.dir, "CollectedURL.txt"))

		if self.karepmu.scanport:
			copyfile("tmp/port", os.path.join(self.dir, "Ports.txt"))
			print(""+colors.warnaihidupku("red")+"\t|\n\t|___"+colors.warnaihidupku("white")+"Ports\n\t\t"+colors.warnaihidupku("red")+"|__"+colors.warnaihidupku("green")+""+os.path.join(self.dir, "Ports.txt"))

		if self.karepmu.emaildiscover:
			copyfile("tmp/mail", os.path.join(self.dir, "Email.txt"))
			print(""+colors.warnaihidupku("red")+"\t|\n\t|___"+colors.warnaihidupku("white")+"Email\n\t\t"+colors.warnaihidupku("red")+"|__"+colors.warnaihidupku("green")+""+os.path.join(self.dir, "Email.txt"))

		if self.karepmu.filesensitive:
			copyfile("tmp/file", os.path.join(self.dir, "Sensitive_Files.txt"))
			print(""+colors.warnaihidupku("red")+"\t|\n\t|___"+colors.warnaihidupku("white")+"Sensitive_File\n\t\t"+colors.warnaihidupku("red")+"|__"+colors.warnaihidupku("green")+""+os.path.join(self.dir, "Sensitive_Files.txt"))
