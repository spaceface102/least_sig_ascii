#!/usr/bin/python3
from getpass import getpass
from lookups import asciiallow
import sys
import numpy as np
import random


default_write_file = "write.txt"
default_read_file = "read.txt"

def get_message(prompt = "Enter Message: "):
	getpass(prompt = prompt)
	mes_bytes = bytes(get_message(), encoding = "utf8")
	mes_bits = np.unpackbits(np.array(list(mes_bytes), dtype = 'u1'))
	return mes_bits

def randchars_encode(data_bits, f_name = default_write_file):
	'''f_name by default is defined by default_file_name'''
	out_bytes = [random.choice(asciiallow[bit]) for bit in mes_bits]
	out_bytes = np.array(out_bytes, dtype = 'u1')
	with open(f_name, "wb") as f:
		f.write(out_bytes)

def randchars_decode(f_name = default_read_file):
	pass

def main():
	sys_accept_args = {
	"encode" : {"encode", "e", "enc"}, 
	"decode" : {"decode", "d", "dec"}, 
	"output" : {"o", "out","output", "name", "fname"}]
	sys_define_args = {
	"encode" : False, "decode" : False,
	"output" : [d



randchars_encode(f_name = "newnew.txt")

if __name__ == "__main__":
	if len(sys.argv) == 1:
		pass
	if len(sys.argv) > 1:
		pass
