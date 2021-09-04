import importlib
import importlib.util
import os
import requests
import sys



slyexists = importlib.util.find_spec("sly") is not None
nuitkaexists = importlib.util.find_spec("nuitka") is not None
playsoundexists = importlib.util.find_spec("playsound") is not None

#print(slyexists)

if slyexists == True:
    print("SLY exists. No need to install.")

else:
    print("Sly does not exist. Installing...")
    os.system("pip install sly")


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
	sudo bash build.sh -linux

	""")



print("AUSL is installed! you can start your own programs using \"sudo ./AUSL.bin <PROGRAM_NAME.ausl>\"")
deeta = input("Run the example program? (Y/N) >> ")
if deeta == "Y" or deeta == "y":
    os.system("sudo ./AUSL.bin myprogram.ausl")        
