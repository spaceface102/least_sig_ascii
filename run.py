#!/usr/bin/python3
from lookups import asciiallow
from getpass import getpass
from random import choice
from sys import argv
import numpy as np

class ascii_map:
	'''Take in input as bytes and map each bit of every byte 
	to a new byte that whose least significant bit is the same'''
	def __init__(self):
		self.nameread = "stdout.txt"
		self.namewrite = "stdout.txt"
		self.bytes = None
		self.encoded = None
		self.decoded = None

	def get_message(self, prompt = "Enter Message: ", encoding = "utf-8"):
		mess_bytes = bytes(getpass(prompt = prompt), encoding = encoding)
		self.bytes = np.array(list(mess_bytes), dtype = 'u1')

	def read_file_bytes(self):
		with open(self.nameread, "rb") as f:
			npbytes = np.array(list(f.read()), dtype = 'u1')
		self.bytes = npbytes

	def write_file_bytes(self, data):
		"data should either be self.decoded or self.encoded"
		with open(self.namewrite, "wb") as f:
			f.write(data)

	def randbytes_encode(self):
		self.encoded = np.unpackbits(self.bytes)
		for i, bit in enumerate(self.encoded):
			self.encoded[i] = choice(asciiallow[bit])

	def randbytes_decode(self):
		self.decoded = np.packbits(self.bytes&1)

	def change_readname(self, fname):
		self.nameread = fname
	
	def change_writename(self, fname):
		self.namewrite = fname

def handleargs():
	args = [arg.replace("-", "") for arg in argv[1:]]
	accept_args = [ {"encode", "e", "enc"}, #0
 					{"decode", "d", "dec"}, #1
 					{"output", "o", "out"} ]#2 
	decode_encode_count = output_count = i = 0
	while i < len(args):
		for j, accept in enumerate(accept_args):
			if args[i] in accept:
				decode_encode_count += int(j == 0 or j == 1)
				output_count += int(j == 2)
		if decode_encode_count > 1 and decode_encode_count != output_count:
			print("Please define an output for each encode and decode!")
			#else use default output self.nameread/write	
		decode_encode_count = output_count = 0

if __name__ == "__main__":