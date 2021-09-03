nuitkacommand="python3 -m nuitka"
pythoncommand="python3"
slycommand="python3 -m sly"


printf "checking dependencies...\n"
	

	#Test if dependencies are met
	if ! command -v python3 &> /dev/null;
	then
		printf "Python3 dependency check failed. Installing Python3...\n"
		sudo apt-get install python3
		exit

	else
		printf "Python3 depecdency check succeeded. no need to install python3.\n"

	fi



	if ! command -v $nuitkacommand &> /dev/null;
	then
		printf "nuitka dependency check failed. Installing nuitka...\n"
		sudo pip install nuitka
		exit
		
	else
		printf "nuitka dependency check succeeded. no need to install nuitka module.\n"
	
	fi
	
	if ! command -v $slycommand &> /dev/null;
	then
		printf "sly dependency check failed. Installing nuitka...\n"
		sudo pip install sly
		exit
		
	else
		printf "sly dependency check succeeded. no need to install sly module.\n"
	
	fi
	
	
	sleep 3
	
	
	printf "pulling AUSL from github repository...\n"
	mkdir AUSL_latest
	cd AUSL_latest
	wget https://raw.githubusercontent.com/MEMESCOEP/AUSL/main/AUSL.py
	wget https://raw.githubusercontent.com/MEMESCOEP/AUSL/main/build.sh
	wget https://raw.githubusercontent.com/MEMESCOEP/AUSL/main/myprogram.ausl
	wget https://raw.githubusercontent.com/MEMESCOEP/AUSL/main/ome.wav
	sudo bash build.sh -verbose -linux -runonbuild
	

