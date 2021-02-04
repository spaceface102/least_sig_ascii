#!/usr/bin/python3
from getpass import getpass
from lookups import asciiallow
import sys
import numpy as np
import random


default_write = "stdout.txt"
default_read = "stdin.txt"
def_rw = [default_read, default_write]

def get_message(prompt = "Enter Message: ", encoding = "utf-8"):
	mes_bytes = bytes(getpass(prompt = prompt), encoding = encoding)
	mes_bits = np.unpackbits(np.array(list(mes_bytes), dtype = 'u1'))
	return mes_bits

def get_file(f_name = default_read):
	with open(f_name, "rb") as f:
		data_bytes = np.array(list(f.read()), dtype = 'u1')
	return np.packbits(data_bytes&1)

def randchars_encode(data_bits, f_name = default_write):
	'''f_name by default is defined by default_file_name'''
	for i, bit in enumerate(data_bits): 
		'''use the same array to avoid allocating more memory
		but data_bits is now an array filled with the ascii values
		associated with the bits in data_bits'''
		data_bits[i] = random.choice(asciiallow[bit])
	with open(f_name, "wb") as f:
		f.write(data_bits)

def randchars_decode(data_bytes, f_name = default_read):
	with open(f_name, "wb") as f:
		data_bytes = d
		f.write(data_bytes)

def main(do_encode = False, do_decode = False, rw = def_rw):
	sys_accept_args = {
	"encode" : {"encode", "e", "enc"}, 
	"decode" : {"decode", "d", "dec"}, 
	"output" : {"o", "out", "output"},
	"input"  : {"i", "in", "input"}}
	print(rw)
	rw = "hello", "party"
	rw = "yo", "dude"
	print(rw)

if __name__ == "__main__":
	if len(sys.argv) == 1:
		randchars_encode(get_message())
		print(f'''Rec. usage: {sys.argv[0]} -e <file> -d <file> -o <file>''')
		print("e == encode, d == decode, o == output")
		print(f"Open file {default_write} to see program output!")

	if len(sys.argv) > 1:
		main()	
