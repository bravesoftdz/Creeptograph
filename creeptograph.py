#creeptograph
from __future__ import print_function
import string
import sys
def decryption():
	print("Enter text")
	text = raw_input("> ")
	print("\n")
	en = {'g':'a', 'a':'b', 's':'c', '4':'d', '2':'e','3':'f','m':'g', 'c':'h', 'f':'i', 'r':'j', 'q':'k', '1':'l', 'd':'m', '9':'n', '0':'o', 't':'p', 'b':'q', 'n':'r', 'x':'s', 'j':'t', 'z':'u', 'p':'v', '8':'w', '7':'x', 'v':'y', '5':'z', " ": " ", ".":".", ",":",", "!":"!", "?":"?"}
	for letter in text:
    		print(en[letter], end='')
	print("\n")
def exit():
	exit(0)
def encryption():
	print("Enter text")
	text = raw_input("> ")
	print("\n")
	en = {'a':'g', 'b':'a', 'c':'s', 'd':'4', 'e':'2','f':'3','g':'m', 'h':'c', 'i':'f', 'j':'r', 'k':'q', 'l':'1', 'm':'d', 'n':'9', 'o':'0', 'p':'t', 'q':'b', 'r':'n', 's':'x', 't':'j', 'u':'z', 'v':'p', 'w':'8', 'x':'7', 'y':'v', 'z':'5', " ": " ", ".":".", ",":",", "!":"!", "?":"?"}
	for letter in text:
    		print(en[letter], end='')
	print("\n")
def banner():
	print("Creeptograph")
	print("Very simple encryptor. Converts all lower case alphabet, the dot, comma, exclamation mark, question mark and the space. Nothing else can be converted")
	print("		1. Encrypt")
	print("		2. Decrupt")
	print("		3. Exit")
	opt = raw_input("> ")
	if opt == "1":
		encryption()
	elif opt == "2":
		decryption()
	else:
		exit()
banner()