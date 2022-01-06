import subprocess 
import xml.etree.ElementTree as ET
from lib.manage import file
from lib.color import pelangitapibukangay as colors


class scan():
	def __init__(self,hostlist):
		print("\n"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("blue")+"+"+colors.warnaihidupku("white")+"] Scanning Port\t")
		print("---------------------------------")
		self.process()



	def process(self):
		save = {}
		data = {}
		subprocess.getoutput("nmap -oX tmp/port -p 21,22,23,25,53,80,110,115,135,139,143,194,443,445,1433,3306,3389,5632,5900,25565 --open -iL tmp/ip")
		tree = ET.parse('tmp/port')
		for i in tree.findall('host'):
			ip = i.find("address").get("addr")
			for ii in i.findall("ports"):
				ports = ""
				for iii in ii.findall("port"):
					port = iii.get("portid")
					service = iii.find("service").get("name")
					ps = port+"/"+service+"|"
					ports += ps
				data[ip] = ports
		save['ports'] = [data]
		open("tmp/port", "w")
		for i in save['ports']:
			for i in list(i):
				port_service = save['ports'][0][i][:-1]
				open("tmp/port", "a").write(i+ " ["+port_service+"]\n")
		open("tmp/port", "w")
		for i in save['ports']:
			for i in list(i):
				port_service = save['ports'][0][i][:-1]
				file.save("port", i+ " ["+port_service+"]")
				print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("green")+">"+colors.warnaihidupku("white")+"] "+i+ " "+colors.warnaihidupku("red")+"["+colors.warnaihidupku("green")+""+port_service+""+colors.warnaihidupku("red")+"]")


