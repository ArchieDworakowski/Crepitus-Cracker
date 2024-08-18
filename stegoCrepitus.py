import os

os.system("binwalk -Mez *")

files = os.listdir()

for i in files:
	if i[0] == "_":
		print("possible steganography in " + i)
