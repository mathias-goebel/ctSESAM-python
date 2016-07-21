#!/usr/bin/python3
# -*- coding: utf-8 -*-
import getpass
import pyperclip
import linecache
from hashlib import pbkdf2_hmac

lower_case_letters = list("abcdefghijklmnopqrstuvwxyz")
upper_case_letters = list("ABCDEFGHJKLMNPQRTUVWXYZ")
numbers = list("0123456789")
special_characters = list("""!"@ $%&/()=?'`*+~#-_.,;:{[]}\<>""")
password_characters = lower_case_letters + upper_case_letters + numbers + special_characters

# using a line of your private ssh key as salt
user = getpass.getuser()
ssh = "/home/" + user + "/.ssh/id_rsa"
salt = linecache.getline(ssh, 17)

def convert_bytes_to_password(hashed_bytes, length):
	number = int.from_bytes(hashed_bytes, byteorder="big")
	password = ""
	while number > 0 and len(password) < length:
		password = password + password_characters[number % len(password_characters)]
		number = number // len(password_characters)
	return password

master_password = getpass.getpass('Password:')
domain = input("Domain: ")

while len(domain) < 1:
	print("Bitte gib eine Domain an, für die das Passwort generiert werden soll.")
	domain = input("Domain: ")
hash_string = domain + master_password
hashed_bytes = pbkdf2_hmac("sha512", hash_string.encode("utf-8"),
salt.encode("utf-8"), 4096)
pw = convert_bytes_to_password(hashed_bytes, 20)
pyperclip.copy( pw )
print("Passwort wurde in die Zwischenablage gelegt.")
