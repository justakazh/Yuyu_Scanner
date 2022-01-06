import requests
from multiprocessing.dummy import Pool
from lib.manage import file
from lib.color import pelangitapibukangay as colors
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



def check(host):
	print("\n"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("blue")+"+"+colors.warnaihidupku("white")+"] Checking HTTP/S From Live Host\t")
	print("---------------------------------")
	x = Pool(len(host))
	x.map(process, host)
	x.close()
	x.join()

	# ress = file.openner("file")
	# print("\n\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("red")+"*"+colors.warnaihidupku("white")+"] Total Found : "+colors.warnaihidupku("green")+str(len(ress)))



def process(domain):
	try:
		pecah = domain.split(" ")[0]
		r = requests.get("http://"+pecah, allow_redirects=False)
		print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("green")+">"+colors.warnaihidupku("white")+"] "+ r.url + " "+colors.warnaihidupku("red")+"["+colors.warnaihidupku("green")+"OK"+colors.warnaihidupku("red")+"] ")
	except Exception as e:
		pass	
		# print("http://"+pecah, "Bad Connection")
