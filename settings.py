import os
import json

settings_path = "settings.json"

def Show_Set(settings):
	print("\nCurrent path is: \n", settings[0], "\nCurrent temp path is: \n", settings[1])
def Take_Set():
	settings = []
	run = True
	while run == True:
		target_dir = input("Giwe me a target path\n")
		if os.path.exists(target_dir):
			settings.append(target_dir)
		temp_dir = input("Giwe me a temp path\n")
		if os.path.exists(temp_dir):
			settings.append(temp_dir)
		run = False

	return(settings)
	
def Write_Set(settings):
	with open(settings_path, "w") as set_file:
		json.dump(settings, set_file)
def Read_Set():
	with open(settings_path, "r") as set_file:
		settings = json.load(set_file)
		return(settings)

