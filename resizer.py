from PIL import Image
import os

def Resize(file, path):
	file_path = path + "/" + file
	print(file_path)
	image = Image.open(file_path)
	image = image.convert('RGB')
	image = image.save(path + "/" + file.split(".")[0] + ".jpg", quality=80)
	if file.split(".")[1] != "jpg":
		os.remove(file_path)
	#
	#image.resize((160,300),Image.ANTIALIAS)
	#image.save("new.jpg", compress_level=48)
	#if image.format.lower() in ['jpg']:
	#	image.resize((160,300),Image.ANTIALIAS)
	#	image.save("new.jpg", compress_level=48)