import requests
import socket
import subprocess as sp
from lib.manage import file
from multiprocessing.dummy import Pool
from lib.color import pelangitapibukangay as colors

def check(hostlist):
	print("\n"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("blue")+"+"+colors.warnaihidupku("white")+"] Checking Live Host & IP Address \t")
	print("---------------------------------")
	x = Pool(len(hostlist))
	x.map(process, hostlist)
	x.close()
	x.join()
	live = file.openner("hostlive")
	die = file.openner("hostdie")
	print("\n\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("red")+"*"+colors.warnaihidupku("white")+"] Total Live : "+colors.warnaihidupku("green")+str(len(live)))
	print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("red")+"*"+colors.warnaihidupku("white")+"] Total Die : "+colors.warnaihidupku("green")+str(len(die)))



def process(domain):
	try:
		check = socket.gethostbyname(domain)
		if check:
			if domain+" ["+check+"]" not in file.openner("hostlive"):
				print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("green")+">"+colors.warnaihidupku("white")+"] "+ domain + " "+colors.warnaihidupku("red")+"["+colors.warnaihidupku("green")+"Live"+colors.warnaihidupku("red")+"] "+colors.warnaihidupku("red")+"["+colors.warnaihidupku("green")+str(check)+colors.warnaihidupku("red")+"] ")
				file.save("hostlive", domain+" ["+check+"]")
				
			if check not in file.openner("ip"):
				file.save("ip", check)

			if domain not in file.openner("http"):
				file.save("http", domain)
		else:
			print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("red")+"-"+colors.warnaihidupku("white")+"] "+ domain + " "+colors.warnaihidupku("red")+"["+colors.warnaihidupku("cyan")+"Die"+colors.warnaihidupku("red")+"] ")
			file.save("hostdie", domain)

	except Exception as e:
		print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("red")+"-"+colors.warnaihidupku("white")+"] "+ domain + " "+colors.warnaihidupku("red")+"["+colors.warnaihidupku("cyan")+"Die"+colors.warnaihidupku("red")+"] ")
		file.save("hostdie", domain)
		pass
