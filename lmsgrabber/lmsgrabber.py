import urllib2
import urllib
import getopt
import sys
import string
import json
import os

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
	print(url)
	jsessionId = "was9hsuug3c4mc2l7scvhhgk"
	start, end = string.split(url, "?")
	start = string.rsplit(start, "/", 3)[0]
	print(start)
	
	try:
		f = urllib2.urlopen(url)
		for line in f:
			if "<iframe " in line:
				sectionId = string.split(string.split(line, "section/", 1)[1], "?", 1)[0]
	except urllib2.URLError, e:
		print(e)
		exit(0)
	
	api = start + "/client/api/sections/" + sectionId + "/section-data.json?skipCache=false&pageIndex=1&pageSize=50"
	print(api)
	sectiondata = ""
	try:
		#print("URL Opened")
		opener = urllib2.build_opener()
		if jsessionId is not None:
			opener.addheaders.append(('Cookie', 'jsessionid=' + jsessionId))
		f = opener.open(api)
		#print("API Call Made")
		sectiondata = f.read()
	except urllib2.URLError, e:
		print(e)
		exit(0)
	print(sectiondata)
	#input()
	
	
	return None
	
	data = json.loads(sectiondata)
	#print(json.dumps(data, indent=2))
	num = data["section"]["presentations"]["totalResults"]
	vidnumber = num
	course = data["section"]["course"]["identifier"]
	print("Unit: " + course)
	if not os.path.isdir(course):
		os.mkdir(course)
	print("Number Of Results: " + str(num))
	videos = []
	for content in data["section"]["presentations"]["pageContents"]:
		videos.append([vidnumber, str(content["richMedia"] + "/mediacontent.m4v"), str(content["startTime"][0:10])])
		#print(vidnumber)
		#print(content["week"])
		#print(content["richMedia"] + "/mediacontent.m4v")
		#print(content["startTime"])
		#print(content["startTime"][0:10])
		vidnumber -= 1
	videos.reverse()
	for video in videos:
		#print(video)
		if not os.path.exists(course + "/" + str(video[0]) + " " + video[2] + ".m4v"):
			urllib.urlretrieve(video[1], course + "/" + str(video[0]) + " " + video[2] + ".m4v")
			print(course + "/" + str(video[0]) + " " + video[2] + ".m4v - Download Complete")
		else:
			print(course + "/" + str(video[0]) + " " + video[2] + ".m4v - Already Exists")
	


if __name__ == '__main__':
	main(sys.argv[1:])

