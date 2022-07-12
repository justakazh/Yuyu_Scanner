import os
import datetime
import json
class generate:
	"""docstring for generate"""
	def __init__(self, save, output, domain, data):

		# generate folder output 
		# pwd = os.getcwd()
		date = str(datetime.datetime.now().date())
		fromdate = os.path.join(output, "output",date)
		folder = os.path.join(fromdate, domain)
		try:
			os.makedirs(folder, exist_ok=True)
		except:
			pass


		# subdomain 
		if save == "subdomainfinder":
		 	location = os.path.join(folder, "subdomain.txt")
		 	open(location, "w")
		 	for subdo in data:
		 		open(location, "a").write("%s\n" % (subdo))

		if save == "checklive":
		 	location = os.path.join(folder, "livehost.txt")
		 	location_ip = os.path.join(folder, "ip.txt")
		 	open(location, "w")
		 	for host in data:
		 		open(location, "a").write("%s | %s\n" % (host[0], host[1]))
		 		open(location_ip, "a").write("%s" % (host[1]))

		if save == "checkprotocol":
		 	location = os.path.join(folder, "protocol.txt")
		 	open(location, "w")
		 	for proto in data:
		 		open(location, "a").write("%s\n" % (proto))

		if save == "revip":
		 	location = os.path.join(folder, "reverseip.txt")
		 	open(location, "w")
		 	for domain in data:
		 		open(location, "a").write("%s\n" % (domain))

		if save == "filesensitive":
		 	location = os.path.join(folder, "files.txt")
		 	open(location, "w")
		 	for file in data:
		 		open(location, "a").write("%s\n" % (file))


		if save == "whois":
		 	location = os.path.join(folder, "whois.txt")
		 	open(location, "w")
		 	open(location, "a").write("%s\n" % (data))

		if save == "scanport":
		 	location = os.path.join(folder, "portscan.txt")
		 	open(location, "w")
		 	for ip in data:
		 		open(location, "a").write("%s\n" % ("%s" % (ip[0])))
		 		for port in ip[1]:
		 			open(location, "a").write("\tPort %s (%s) is %s" % (port[0], port[1], port[2]))


		if save == "securityheaders":
		 	location = os.path.join(folder, "securityheaders.txt")
		 	open(location, "w")
		 	for sechead in data:
		 		for sec in sechead:
		 			open(location, "a").write("\n%s \n" % (sec))
		 			for val in sechead[sec]:
		 				open(location, "a").write("\t- %s \n" % (val))

		if save == "corscheck":
		 	location = os.path.join(folder, "cors.txt")
		 	open(location, "w")
		 	for domain in data:
		 		open(location, "a").write("%s\n" % (domain))

		if save == "checktech":
			location = os.path.join(folder, "technologies.txt")
			open(location, "w")
			for tech in data:
				open(location, "a").write("\n%s \n\tStatus Code :  %s \n\tTitle : %s \n\tTechnologies : " % (tech[0], str(tech[1]), tech[3]))
				for vendor in tech[2]:
					open(location, "a").write("\n\t\t - %s : %s" % (vendor, tech[2][vendor]['versions']))

		if save == "emailsearch":
			location = os.path.join(folder, "email.txt")
			open(location, "w")
			for mail in data:
				open(location, "a").write("%s\n" % (mail))


		if save == "collecturl":
			location = os.path.join(folder, "waybackurl.txt")
			open(location, "w")
			open(location, "a").write("\n".join(data))
		
		if save == "extracturi":
			location_uri = os.path.join(folder, "waybackurl_uri.txt")
			open(location_uri, "w")
			open(location_uri, "a").write("\n".join(data))
			
		if save == "extractjs":
			location_js = os.path.join(folder, "waybackurl_js.txt")
			open(location_js, "w")
			open(location_js, "a").write("\n".join(data))

		if save == "extractfiles":
			location_files = os.path.join(folder, "waybackurl_files.txt")
			open(location_files, "w")
			open(location_files, "a").write("\n".join(data))

		if save == "extractfiles":
			location_document = os.path.join(folder, "waybackurl_document.txt")
			open(location_document, "w")
			open(location_document, "a").write("\n".join(data))
					
		# create json output
		# location = os.path.join(folder, "result.json")
		# open(location, "w")
		# json_data = {
		# 	"target" : domain,
		# 	"subdomain": subdomain,
		# 	"protocol": protocol,
		# 	"livehost": livehost,
		# 	"reverseip": reverseip,
		# 	"files": files,
		# 	"whois": whois,
		# 	"portscan": portscan,
		# 	"securityheaders": securityheaders,
		# 	"cors": cors,
		# 	"technologies": technologies,
		# 	"email": email,
		# 	"wayback": "sorry, the possibility of this data will be large. so we recommend you to take a look at the wayback.txt to avoid crashing the browser",
		# 	"wayback_files": "sorry, the possibility of this data will be large. so we recommend you to take a look at the wayback_files.txt to avoid crashing the browser",
		# 	"wayback_uri": "sorry, the possibility of this data will be large. so we recommend you to take a look at the wayback_uri.txt to avoid crashing the browser",
		# 	"wayback_document": "sorry, the possibility of this data will be large. so we recommend you to take a look at the wayback_document.txt to avoid crashing the browser",
		# 	"wayback_js": "sorry, the possibility of this data will be large. so we recommend you to take a look at the wayback_js.txt to avoid crashing the browser",
		# 	"timeout": timeout
		# }
		# j = json.dumps(json_data, indent=4)
		# open(location, "a").write(j)
		# print(j)