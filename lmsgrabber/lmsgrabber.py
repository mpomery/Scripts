import urllib2
import getopt
import sys
import string
import json

verstring = "0.1"

def version():
	print("LMS Grabber")
	print("Made By: Mitchell \"Pommers\" Pomery")
	print("Version: " + verstring)
	exit(0)

def main(argv):
	if len(argv) != 1:
		version()
	url = argv[0]
	#print(url)
	start, params = string.split(url, ";", 1)
	opts = string.split(params, "?")
	#print(start)
	#print(params)
	#print(opts)
	jsessionId = None
	sectionId = None
	for opt in opts:
		name, val = string.split(opt, "=", 1)
		if name == "sectionId":
			sectionId = val
		elif name == "jsessionid":
			jsessionId = val
	#print(sectionId)
	
	api = string.rsplit(start, "/", 2)[0] + "/api/" + sectionId + "/section-data.json?skipCache=false&pageIndex=1&pageSize=50"
	#print(api)
	sectiondata = ""
	try:
		# Open the URL to look legit
		f = urllib2.urlopen(url)
		#print("URL Opened")
		opener = urllib2.build_opener()
		opener.addheaders.append(('Cookie', 'jsessionid=' + jsessionId))
		f = opener.open(api)
		#print("API Call Made")
		sectiondata = f.read()
	except urllib2.URLError, e:
		print(e)
		exit(0)
	print(sectiondata)
	#input()
	data = json.loads(sectiondata)
	#print(json.dumps(data, indent=2))
	num = data["section"]["presentations"]["totalResults"]
	print("Number Of Results: " + str(num))
	for content in data["section"]["presentations"]["pageContents"]:
		print(content["week"])
		print(content["richMedia"])
	


if __name__ == '__main__':
	main(sys.argv[1:])

