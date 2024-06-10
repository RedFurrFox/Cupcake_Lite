import os


def clear_terminal():
	"""
	Clears up the output terminal
	"""
	if os.name == "nt":  # Check if the OS is Windows
		os.system("cls")
	else:
		os.system("clear")

def posix_type():
	"""
	Returns the appropriate file navigation type based on the operating system.
	"""
	if os.name == "nt":  # Check if the OS is Windows
		return "/"
	else:
		return "\\"
