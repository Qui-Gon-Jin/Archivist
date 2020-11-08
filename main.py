import os
import walk
import resizer
import archivist
import settings

def main():
	while True:
		os.system('cls||clear')
		set_pack = settings.Read_Set()

		choose = input("\tMain menu\n1 - Run\n2 - Set\n3 - Exit\n")
		if choose == "1":
			try:
				os.mkdir(set_pack[1])
			except OSError:
				print ("Создать директорию %s не удалось" % set_pack[1])

			zip_list = walk.Walk(set_pack[0])
			for i in zip_list:
				archivist.Unpack(set_pack, i)
				file_list = walk.Walk(set_pack[1])
				for image in file_list:
					resizer.Resize(image, set_pack[1])
				archivist.Pack(set_pack, i)

		elif choose == "2":
			settings.Show_Set(set_pack)
			if input("\nDo you want to change something? (1 to yess)\n") == "1":
				set_pack = settings.Take_Set()
				settings.Write_Set(set_pack)
				print("\nCurrent set is: ")
				settings.Show_Set(set_pack)
				input()

		elif choose == "3":
			break
		else:
			print("something went wrong")

if __name__ == "__main__":
	main()