from colorama import Fore,Back,init


def warnaihidupku(color):
	if color == "red":
		return '\033[91m'
	if color == "blue":
		return '\033[94m'
	if color == "green":
		return '\033[92m'
	if color == "white":
		return '\033[00m'
	if color == "cyan":
		return '\033[0;96m'
	if color == "yellow":
		return '\033[0;93m'