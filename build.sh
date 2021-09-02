#variable initialization
nuitkacommand="python3 -m nuitka"
pythoncommand="python3"
ronb="false"
cpu_type=$(uname -i)





function build_failed ()
{
	printf "\nCompilation failed.\n"
	exit
}




function build_done ()
{
	if [ "$ronb" = "true" ]; then
		printf "\nRunning Program...\n"
		sudo ./AUSL.bin myprogram.ausl
	fi
	exit	
}


#Handle Build
function Main_Func () 
{

#Test if first argument is empty
if [ "$1" = "" ]; then

	printf "\nAUSL Build Script\n"
	printf "[HOW TO RUN] sudo bash build.sh -[OS] -[verbose] -[runonbuild]\n"
	printf "[OS]: -Linux, -win32\n"
	printf "[verbose]: -verbose, <empty>\n"
	printf "[runonbuild]: -runonbuild, <empty>\n"
	
	
else
	#first argument is not empty, we can continue the compilation
	printf "checking dependencies...\n"
	

	#Test if dependencies are met
	if ! command -v python3 &> /dev/null;
	then
		printf "Python3 dependency check failed.\n"
		exit

	else
		printf "Python3 depecdency check succeeded.\n"

	fi



	if ! command -v $nuitkacommand &> /dev/null;
	then
		printf "nuitka dependency check failed.\n"
		exit
		
	else
		printf "nuitka dependency check succeeded.\n"
	
	fi



	#All dependencies are good, continue.
	printf "Done! All dependencies succeeded.\n\n\n\n\n"


	sleep 1


#echo Building AUSL from AUSL.py...
#POSITIONAL=()



	#Test if arguments contain "-win32"
	#Builds for win32
	if [[ "$1" = "-win32" ]] || [[ "$2" = "-win32" ]] || [[ "$3" = "-win32" ]]; then
	#sudo python3 -m nuitka --windows --standalone --onefile --follow-imports AUSL.py
		printf "cross-compiling for win32 is not yet supported.\n"
	

	#Test if arguments contain "-win32"
	#Builds for Linux
	else if [[ "$1" = "-linux" ]] || [[ "$2" = "-linux" ]] || [[ "$3" = "-linux" ]]; then
	
			printf "Building for Linux"
		if [[ "$1" = "-verbose" ]] || [[ "$2" = "-verbose" ]] || [[ "$3" = "-	verbose" ]]; then
			printf "Verbose is enabled.\n"
			sudo python3 -m nuitka --standalone --onefile --verbose --follow-imports AUSL.py || build_failed
			sudo rm -rf AUSL.build
			sudo rm -rf AUSL.dist
			printf "\nCompilation done.\n"
			build_done
			#sudo ./AUSL.bin myprogram.ausl

		else
			sudo python3 -m nuitka --standalone --onefile --follow-imports AUSL.py || build_failed
			printf "\nCompilation done.\n"
			build_done
			sudo rm -rf AUSL.build
			sudo rm -rf AUSL.dist
			#sudo ./AUSL.bin myprogram.ausl
		fi
		
		
	fi
	fi
fi

}



#Test if arguments contain "-runonbuild"
if [[ "$3" = "-runonbuild" ]] || [[ "$2" = "-runonbuild" ]] || [[ "$1" = "-runonbuild" ]]; then
ronb="true"
			#printf "Running program...\n"
			#sudo ./AUSL.bin myprogram.ausl
fi


printf "cpu type: $cpu_type\n\n\n\n\n"
uname -a


Main_Func "$1" "$2" "$3"


