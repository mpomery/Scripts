import urllib2
import urllib
import string
import os

url = "http://www.deegan.id.au/temp/20140918-ucc-40th/"
pics = []
folder = "pics"

try:
	f = urllib2.urlopen(url)
	for line in f:
		if "<img src=" in line:
			pics.append(string.split(string.split(line, "Thumbnail ", 1)[1], " ", 1)[0])
except urllib2.URLError, e:
	print(e)
	exit(0)

if not os.path.exists(folder):
	os.mkdir(folder)

for pic in pics:
	print(pic)
	if not os.path.exists(folder + "/" + pic):
		urllib.urlretrieve(url + pic, folder + "/" + pic)
		print(folder + "/" + pic + " - Download Complete")
	else:
		print(folder + "/" + pic + " - Already Exists")

print pics

