from lib.subdo import threatcrowd
from lib.subdo import urlscan
from lib.subdo import rapiddns
from lib.subdo import alienvault
from lib.subdo import dnsdumpster
from lib.subdo import crtsh
from lib.subdo import threatminer
from lib.subdo import certspotter
from lib.subdo import hackertarget
from lib.subdo import riddler
from lib.subdo import commoncrawl
from lib.color import pelangitapibukangay as colors
import threading

def find(domain):
	print("\n"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("blue")+"+"+colors.warnaihidupku("white")+"] Searching Subdomain For: "+domain+"\t")
	print("---------------------------------")
	th = [
		threading.Thread(target=threatcrowd.data, args=(domain, )),
		threading.Thread(target=urlscan.data, args=(domain, )),
		threading.Thread(target=rapiddns.data, args=(domain, )),
		threading.Thread(target=alienvault.data, args=(domain, )),
		threading.Thread(target=dnsdumpster.data, args=(domain, )),
		threading.Thread(target=crtsh.data, args=(domain, )),
		threading.Thread(target=threatminer.data, args=(domain, )),
		threading.Thread(target=certspotter.data, args=(domain, )),
		threading.Thread(target=hackertarget.data, args=(domain, )),
		threading.Thread(target=riddler.data, args=(domain, )),
		threading.Thread(target=commoncrawl.data, args=(domain, )),
	]
	for i in th:
		i.start()
	for i in th:
		i.join()

	# filter subdo
	asw = []
	liss = [i.strip() for i in open("tmp/subdomain", "r").readlines()]
	for i in liss:
		if domain not in i:
			pass
		else:
			asw.append(i)
	subdomain = list(dict.fromkeys(asw))
	open("tmp/subdomain", "w")
	for subdo in subdomain: 
		if subdo != "" and "*." not in subdo and ":" not in subdo:
			open("tmp/subdomain", "a").write(subdo+"\n")
			print("\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("green")+">"+colors.warnaihidupku("white")+"] " + subdo)
	hitung = len([i.strip() for i in open("tmp/subdomain", "r").readlines()])
	print("\n\t"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("red")+"*"+colors.warnaihidupku("white")+"] Total Found: "+colors.warnaihidupku("green")+""+str(hitung)+"\n\n")