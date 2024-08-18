import os

os.system("binwalk -Mez *")
import os

files = os.listdir()

for i in files:
	if i[0] == "_" and i[1] == "_" and not i == "final":
		print("possible steganography in " + i)
