#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

files = []
current_directory = os.getcwd()


for file in os.listdir(current_directory):
    if ("encrypt" in file or "decrypt" in file) and ("py" in file or "exe" in file) or file == "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)


with open("thekey.key", "rb") as key:
    secretkey = key.read()

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)
