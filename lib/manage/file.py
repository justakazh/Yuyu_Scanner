from lib.color import pelangitapibukangay as colors
from shutil import copyfile
import datetime
import os
def openner(types):
	if types == "subdomain":
		return [i.strip() for i in open("tmp/subdomain", "r").readlines()]
	if types == "check":
		return [i.strip() for i in open("tmp/check", "r").readlines()]
	if types == "url":
		return [i.strip() for i in open("tmp/url", "r").readlines()]
	if types == "revip":
		return [i.strip() for i in open("tmp/revip", "r").readlines()]
	if types == "mail":
		return [i.strip() for i in open("tmp/mail", "r").readlines()]
	if types == "whois":
		return [i.strip() for i in open("tmp/whois", "r").readlines()]
	if types == "port":
		return [i.strip() for i in open("tmp/port", "r").readlines()]
	if types == "ip":
		return [i.strip() for i in open("tmp/ip", "r").readlines()]
	if types == "file":
		return [i.strip() for i in open("tmp/file", "r").readlines()]
	if types == "hostdie":
		return [i.strip() for i in open("tmp/hostdie", "r").readlines()]
	if types == "hostlive":
		return [i.strip() for i in open("tmp/hostlive", "r").readlines()]
	if types == "information":
		return [i.strip() for i in open("tmp/information", "r").readlines()]
	if types == "seed":
		return [i.strip() for i in open("seed/path.txt", "r").readlines()]
	if types == "http":
		return [i.strip() for i in open("tmp/http", "r").readlines()]
	if types == "headers":
		return [i.strip() for i in open("tmp/headers", "r").readlines()]
	if types == "cors":
		return [i.strip() for i in open("tmp/cors", "r").readlines()]


def save(types, text):
	if types == "subdomain":
		open("tmp/subdomain", "a").write(text+"\n")
	if types == "check":
		open("tmp/check", "a").write(text+"\n")
	if types == "url":
		open("tmp/url", "a").write(text+"\n")
	if types == "revip":
		open("tmp/revip", "a").write(text+"\n")
	if types == "mail":
		open("tmp/mail", "a").write(text+"\n")
	if types == "whois":
		open("tmp/whois", "a").write(text+"\n")
	if types == "port":
		open("tmp/port", "a").write(text+"\n")
	if types == "ip":
		open("tmp/ip", "a").write(text+"\n")
	if types == "file":
		open("tmp/file", "a").write(text+"\n")
	if types == "hostlive":
		open("tmp/hostlive", "a").write(text+"\n")
	if types == "hostdie":
		open("tmp/hostdie", "a").write(text+"\n")
	if types == "information":
		open("tmp/information", "a").write(text+"\n")
	if types == "http":
		open("tmp/http", "a").write(text+"\n")
	if types == "headers":
		open("tmp/headers", "a").write(text+"\n")
	if types == "cors":
		open("tmp/cors", "a").write(text+"\n")


def clear():
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
	open("tmp/headers", "w")
	open("tmp/cors", "w")



def output(target, args):
	date = str(datetime.datetime.now().date())
	pwd = os.getcwd()

	print("\n"+colors.warnaihidupku("white")+"["+colors.warnaihidupku("blue")+"+"+colors.warnaihidupku("white")+"] Output Result\t")
	print("---------------------------------")
	xdir = os.path.join(pwd, "output/"+date+"/"+target)
	try:
		os.makedirs(xdir)
	except:
		pass

	copyfile("tmp/subdomain", os.path.join(xdir, "Subdomain.txt"))
	print(""+colors.warnaihidupku("red")+"\t|\n\t|___"+colors.warnaihidupku("white")+"Subdomain\n\t\t"+colors.warnaihidupku("red")+"|__"+colors.warnaihidupku("green")+""+os.path.join(xdir, "Subdomain.txt"))
	
	if args.checklive:
		copyfile("tmp/hostlive", os.path.join(xdir, "Host_Live.txt"))
		print(""+colors.warnaihidupku("red")+"\t|\n\t|___"+colors.warnaihidupku("white")+"Information\n\t\t"+colors.warnaihidupku("red")+"|__"+colors.warnaihidupku("green")+""+os.path.join(xdir, "Host_Live.txt"))
		copyfile("tmp/ip", os.path.join(xdir, "Ip_Address.txt"))
		print(""+colors.warnaihidupku("red")+"\t|\n\t|___"+colors.warnaihidupku("white")+"Information\n\t\t"+colors.warnaihidupku("red")+"|__"+colors.warnaihidupku("green")+""+os.path.join(xdir, "Ip_Address.txt"))

	if args.collectinginformation:
		copyfile("tmp/information", os.path.join(xdir, "Information.txt"))
		print(""+colors.warnaihidupku("red")+"\t|\n\t|___"+colors.warnaihidupku("white")+"Information\n\t\t"+colors.warnaihidupku("red")+"|__"+colors.warnaihidupku("green")+""+os.path.join(xdir, "Information.txt"))

	if args.whois:
		copyfile("tmp/whois", os.path.join(xdir, "Whois.txt"))
		print(""+colors.warnaihidupku("red")+"\t|\n\t|___"+colors.warnaihidupku("white")+"Whois\n\t\t"+colors.warnaihidupku("red")+"|__"+colors.warnaihidupku("green")+""+os.path.join(xdir, "Whois.txt"))
		
	if args.revip:
		copyfile("tmp/revip", os.path.join(xdir, "ReverseIP.txt"))
		print(""+colors.warnaihidupku("red")+"\t|\n\t|___"+colors.warnaihidupku("white")+"Reverse IP\n\t\t"+colors.warnaihidupku("red")+"|__"+colors.warnaihidupku("green")+""+os.path.join(xdir, "ReverseIP.txt"))

	if args.collecturl:
		copyfile("tmp/url", os.path.join(xdir, "CollectedURL.txt"))
		print(""+colors.warnaihidupku("red")+"\t|\n\t|___"+colors.warnaihidupku("white")+"Collected URL\n\t\t"+colors.warnaihidupku("red")+"|__"+colors.warnaihidupku("green")+""+os.path.join(xdir, "CollectedURL.txt"))

	if args.scanport:
		copyfile("tmp/port", os.path.join(xdir, "Ports.txt"))
		print(""+colors.warnaihidupku("red")+"\t|\n\t|___"+colors.warnaihidupku("white")+"Ports\n\t\t"+colors.warnaihidupku("red")+"|__"+colors.warnaihidupku("green")+""+os.path.join(xdir, "Ports.txt"))

	if args.emaildiscover:
		copyfile("tmp/mail", os.path.join(xdir, "Email.txt"))
		print(""+colors.warnaihidupku("red")+"\t|\n\t|___"+colors.warnaihidupku("white")+"Email\n\t\t"+colors.warnaihidupku("red")+"|__"+colors.warnaihidupku("green")+""+os.path.join(xdir, "Email.txt"))

	if args.filesensitive:
		copyfile("tmp/file", os.path.join(xdir, "Sensitive_Files.txt"))
		print(""+colors.warnaihidupku("red")+"\t|\n\t|___"+colors.warnaihidupku("white")+"Sensitive_File\n\t\t"+colors.warnaihidupku("red")+"|__"+colors.warnaihidupku("green")+""+os.path.join(xdir, "Sensitive_Files.txt"))

	if args.securityheaders:
		copyfile("tmp/headers", os.path.join(xdir, "Missing_Security_Headers.txt"))
		print(""+colors.warnaihidupku("red")+"\t|\n\t|___"+colors.warnaihidupku("white")+"Sensitive_File\n\t\t"+colors.warnaihidupku("red")+"|__"+colors.warnaihidupku("green")+""+os.path.join(xdir, "Missing_Security_Headers.txt"))

	if args.corscheck:
		copyfile("tmp/cors", os.path.join(xdir, "CORS_Missconfiguration.txt"))
		print(""+colors.warnaihidupku("red")+"\t|\n\t|___"+colors.warnaihidupku("white")+"Sensitive_File\n\t\t"+colors.warnaihidupku("red")+"|__"+colors.warnaihidupku("green")+""+os.path.join(xdir, "CORS_Missconfiguration.txt"))

