import os
import zipfile
import shutil
import walk

def Unpack(set_pack, archive_name):
	archive_name = set_pack[0] + "/" + archive_name
	z = zipfile.ZipFile(archive_name, 'r')
	z.extractall(set_pack[1])
	z.close()

def Pack(set_pack, archive_name):
	with zipfile.ZipFile(set_pack[0] + "/" + archive_name, 'w') as myzip:
		myzip.write(set_pack[0] + "/")