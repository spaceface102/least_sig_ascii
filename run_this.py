#!/usr/bin/python3
from getpass import getpass
from lookups import asciiallow
import sys
import numpy as np
import random

def get_message():
	return getpass(prompt = "Enter Message: ")

def find_file():
	pass

def randchars(file_handle = None):
	'''file_handle needs to be able to write/append bytes'''
	mes_bytes = bytes(get_message, encoding = "utf8")
	mes_bits = np.unpackbits(np.array(list(mes_bytes), 'u1'))
	zeros = mes_bits == 0
	ones = mes_bits == 1
	out_bytes = mes_bits #just changing name
	out_bytes[zeros] = random.choice(asciiallow[0])
	out_bytes[ones] = random.choices(asciiallow[1])
	if file_handle:
		file_handle.write(out_bytes)
	else:
		f = open("randchars.txt", "wb")
		f.write(out_bytes)


if __name__ == "__main__":
	if len(sys.argv) == 1:
		pass
	if len(sys.argv) > 1:
		pass
