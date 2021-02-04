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
		self.nameread = "stdin.txt"
		self.namewrite = "stdout.txt"
		self.bytes = None

	def get_message(self, prompt = "Enter Message: ", encoding = "utf-8"):
		mess_bytes = bytes(getpass(prompt = prompt), encoding = encoding)
		self.bytes = np.array(list(mess_bytes), dtype = 'u1')

	def read_file_bytes(self):
		with open(self.nameread, "rb") as f:
			npbytes = np.array(list(f.read()), dtype = 'u1')
		self.bytes = npbytes

	def write_file_bytes(self):
		with open(self.namewrite, "wb") as f:
			f.write(self.bytes)

	def randbytes_encode(self):
		self.bytes = np.unpackbits(self.bytes)
		for i, bit in enumerate(self.bytes):
			self.bytes[i] = choice(asciiallow[bit])

	def randbytes_decode(self):
		self.bytes = np.packbits(self.bytes&1)

	def change_readname(self, fname):
		self.nameread = fname
	
	def change_writename(self, fname):
		self.namewrite = fname

	def default(self):
		self.get_message()
		self.randbytes_encode()
		self.write_file_bytes()
	
	def encode_decode_a_file(self, e=False, d=False, read=None, out=None):
		''''e' indicated encode, 'd' indicates decode, 'read' is 
		read_file_name, 'out' is output file name'''
		if read:
			self.change_readname(read)
		if out:
			self.change_writename(out)
		self.read_file_bytes()
		self.randbytes_encode() if e else self.randbytes_decode()
		self.write_file_bytes()
		self.encoded = self.decoded = None #cleanup

def handle_args():
	args = [arg.replace("-", "") for arg in argv[1:]]
	encode = {"encode", "e", "enc"}
	decode = {"decode", "d", "dec"}
	output = {"output", "o", "out"} 
	for i, arg in enumerate(args):
		if arg in encode:
			e = True
			read = i + 1
		elif arg in decode:
			d = True
			read = i + 1
		elif arg in output:
			out = args[i+1]

if __name__ == "__main__":
	if len(argv) == 1:
		base = ascii_map()
		base.default()
	else:
		handle_args()