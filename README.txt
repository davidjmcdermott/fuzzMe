### Basic Buffer Overflow Practice ###

The included virtual machine is running Windows XP. You will find a target
executable on the desktop named "fuzzMe.exe" which will listen on TCP port
4567, and is vulnerable to a number of buffer overflows. The goal is to
trigger these buffer overflows and use them to gain execution control of the
process, specifically to launch calc.exe. I recommend letting the target
run in the virtual machine, and working from your local machine (nc.exe,
fuzzer, exploits, etc.).

NOTE: The code needed to launch calc.exe is included in the template file


A number of helper files are available in "fuzzMe-files" to get things
started, including the following:

	BOF.ppt		- Basic intro to Buffer Overflows and fuzzing
	nc.exe		- Can be used to interact with the target
				C:\> nc.exe IP_ADDRESS PORT_NUMBER
	fuzzer.py	- Python fuzzing script
	pattern.py	- Python pattern generator
	template.py	- Python template for exploits
	egghunter.py	- Small egghunter for when space is limited
			  such that the exploit code which launches
			  calc.exe will not fit in the most convenient
			  memory.

Inside of "fuzzMe-solutions.7z" are the solutions for each, as well as
the source code for fuzzMe.exe and fuzzMe.dll. This file is password protected.
You are welcome to the password if you like, but I would only recommend that
as a last ditch option.


Hint: Type "HELP" when first connected...


Enjoy!