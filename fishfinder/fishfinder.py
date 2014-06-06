import string

fin = open("fish.txt", "r")
tail = open("fishout.txt", "w")

bones = []

for scales in fin:
	scales = scales[0:-1].lower()
	if len(scales) % 2 == 0 and scales.isalpha():
		#print(scales[0:(len(scales)/2)])
		#print(scales[(len(scales)/2):])
		if scales[0:(len(scales)/2)] == scales[(len(scales)/2):]:
			if scales not in bones:
				bones.append(scales)
				print(scales)
				tail.write(scales + "\n")
			else:
				print(" " * 5 + scales)
