import importlib
import importlib.util
import os
import requests
import sys
import ctypes
import platform

def isAdmin():
	try:
		is_admin = (os.getuid() == 0)
	except AttributeError:
		is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
	return is_admin


pythonpath = ""
for p in sys.path:
    pythonpath = p
    break

print("PYTHON PATH: " + pythonpath)





cwd = os.getcwd()

slyexists = importlib.util.find_spec("sly") is not None
nuitkaexists = importlib.util.find_spec("nuitka") is not None
playsoundexists = importlib.util.find_spec("playsound") is not None
wgetexists = importlib.util.find_spec("wget") is not None


#print(platform.system())




if(platform.system() == "Linux"):


	try:
		#os.system("sudo apt install libjpeg8-dev zlib1g-dev libtiff-dev libfreetype6 libfreetype6-dev libwebp-dev libopenjp2-7-dev libopenjp2-7-dev -y")
		os.system("sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info libcairo2-dev")
		os.system("python3 -m pip install --no-use-pep517  cm-rgb")
		#os.system("""pip3 install  --upgrade --force-reinstall --no-binary ":all:" pycairo""")
		os.system("pip install pygobject")
	except Exception as ex:

																				template = "\nAn exception of type {0} occurred. Arguments:\n{1!r}\n"
																				message = template.format(type(ex).__name__, ex.args)
																				print (bcolors.FAIL + message + bcolors.ENDC)

	#print(slyexists)

	if slyexists == True:
		print("SLY exists. No need to install.")

	else:
		print("Sly does not exist. Installing...")
		os.system("pip install sly")

	if wgetexists == True:
				print("WGET exists. No need to install.")

	else:
		print("WGET does not exist. Installing...")
		os.system("pip install wget")

		

	if nuitkaexists == True:
		print("Nuitka exists. No need to install.")

	else:
		print("Nuitka does not exist. Installing...")
		os.system("pip install nuitka")


	if playsoundexists == True:
		print("playsound exists. No need to install.")

	else:
		print("playsound does not exist. Installing...")
		os.system("pip install playsound")



	path = "./AUSL_latest"

	isdir = os.path.isdir(path)
	if isdir == True:
		print("AUSL_latest path already exists! Please back up any documents that you want to save, as this folder will be deleted.")
		deeta = input("Proceed with installation? (Y/N) >> ")
		if deeta == "Y" or deeta == "y":


					print("Pulling data from server...")
					os.system("""
			rm -rf AUSL_latest
			mkdir AUSL_latest
					cd AUSL_latest
					wget https://raw.githubusercontent.com/MEMESCOEP/AUSL/main/AUSL.py
					wget https://raw.githubusercontent.com/MEMESCOEP/AUSL/main/build.sh
					wget https://raw.githubusercontent.com/MEMESCOEP/AUSL/main/myprogram.ausl
					wget https://raw.githubusercontent.com/MEMESCOEP/AUSL/main/ome.wav
					wget https://raw.githubusercontent.com/MEMESCOEP/AUSL/main/AUSL_COMPILER.py
					wget https://raw.githubusercontent.com/MEMESCOEP/AUSL/main/ausl_runtime.py

					sudo bash build.sh -linux

					""")
		else:
					sys.exit(0)


	else:
		 os.system("""
	mkdir AUSL_latest
		cd AUSL_latest
		wget https://raw.githubusercontent.com/MEMESCOEP/AUSL/main/AUSL.py
		wget https://raw.githubusercontent.com/MEMESCOEP/AUSL/main/build.sh
		wget https://raw.githubusercontent.com/MEMESCOEP/AUSL/main/myprogram.ausl
		wget https://raw.githubusercontent.com/MEMESCOEP/AUSL/main/ome.wav
		wget https://raw.githubusercontent.com/MEMESCOEP/AUSL/main/AUSL_COMPILER.py
		wget https://raw.githubusercontent.com/MEMESCOEP/AUSL/main/ausl_runtime.py

		sudo bash build.sh -linux

		""")



	print("AUSL is installed! you can start your own programs using \"sudo ./AUSL.bin <PROGRAM_NAME.ausl>\"")
	deeta = input("Run the example program? (Y/N) >> ")
	if deeta == "Y" or deeta == "y":
		pathofbin = cwd
		os.system("sudo ./AUSL_latest/AUSL.bin ./AUSL_latest/myprogram.ausl")  
		
		
		
elif(platform.system() == "Windows"):
	print("Win32!")
	try:
		#os.system("sudo apt install libjpeg8-dev zlib1g-dev libtiff-dev libfreetype6 libfreetype6-dev libwebp-dev libopenjp2-7-dev libopenjp2-7-dev -y")
		os.system("sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info libcairo2-dev")
		os.system("python3 -m pip install --no-use-pep517  cm-rgb")
		#os.system("""pip3 install  --upgrade --force-reinstall --no-binary ":all:" pycairo""")
		os.system("pip install pygobject")
	except Exception as ex:

																				template = "\nAn exception of type {0} occurred. Arguments:\n{1!r}\n"
																				message = template.format(type(ex).__name__, ex.args)
																				print (bcolors.FAIL + message + bcolors.ENDC)

	#print(slyexists)

	if slyexists == True:
		print("SLY exists. No need to install.")

	else:
		print("Sly does not exist. Installing...")
		os.system("pip install sly")


	if wgetexists == True:
		print("WGET exists. No need to install.")

	else:
		print("WGET does not exist. Installing...")
		os.system("pip install wget")

		


	if nuitkaexists == True:
		print("Nuitka exists. No need to install.")

	else:
		print("Nuitka does not exist. Installing...")
		os.system("pip install nuitka")


	if playsoundexists == True:
		print("playsound exists. No need to install.")

	else:
		print("playsound does not exist. Installing...")
		os.system("pip install playsound")



	path = ".\\AUSL_latest"
	
	import wget
	urltoDOWNLOAD = "https://raw.githubusercontent.com/MEMESCOEP/AUSL/main/AUSL.py\nhttps://raw.githubusercontent.com/MEMESCOEP/AUSL/main/build.bat\nhttps://raw.githubusercontent.com/MEMESCOEP/AUSL/main/myprogram.ausl\nhttps://raw.githubusercontent.com/MEMESCOEP/AUSL/main/ome.wav\nhttps://raw.githubusercontent.com/MEMESCOEP/AUSL/main/AUSL_COMPILER.py\nhttps://raw.githubusercontent.com/MEMESCOEP/AUSL/main/ausl_runtime.py"
	
	isdir = os.path.isdir(path)
	if isdir == True:
		print("AUSL_latest path already exists! Please back up any documents that you want to save, as this folder will be deleted.")
		deeta = input("Proceed with installation? (Y/N) >> ")
		if deeta == "Y" or deeta == "y":


					print("Pulling data from server...")
					dirtoERASE = (path + "\\")
					for f in os.listdir(dirtoERASE):
											os.remove(os.path.join(dirtoERASE, f))
					for line in urltoDOWNLOAD.splitlines():
											if(line != "" or line != None):
																							print("Getting " + line.rsplit('/', 1)[-1] + " ...")
																							wget.download(line, ".\\" + path + "\\" + line.rsplit('/', 1)[-1])

		else:
					sys.exit(0)


	else:
					 try:
							os.mkdir(".\\AUSL_latest")
					 except:
							0+0
					 print("Pulling data from server...")
					 for line in urltoDOWNLOAD.splitlines():
																							if(line != "" or line != None):
																																															print("Getting " + line.rsplit('/', 1)[-1] + " ...")
																																															wget.download(line, ".\\" + path + "\\" + line.rsplit('/', 1)[-1])

                    


	runbuild = (".\\AUSL_latest\\build.bat" + " " + pythonpath.replace('/', "\\"))
	print("BUILD COMMAND: " + runbuild)
	print("Compiling...")
	os.system(runbuild)
	print("Done.")
	print("AUSL is installed! you can start your own programs using \".\\AUSL.exe <PROGRAM_NAME.ausl>\"")
	deeta = input("Run the example program? (Y/N) >> ")
	if deeta == "Y" or deeta == "y":
		pathofbin = cwd
		os.system("start .\AUSL_latest\AUSL.exe .\AUSL_latest\myprogram.ausl")  
		
		
