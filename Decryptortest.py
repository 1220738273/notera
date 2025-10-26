#!/usr/bin/env python3
import os
import sys
from cryptography.fernet import Fernet
paths = []

if "TESTDIR" not in os.listdir(os.path.dirname(os.path.abspath(__file__))):
     os._exit(0)

for root, dirs, files in os.walk("TESTDIR"):
        for name in files:
            if name.lower().endswith('.notera'):
                paths.append(os.path.join(root, name))

for i in range (len(paths)):
    with open("TEST.key", "r") as key:
         e = Fernet(key.read())
    with open(paths[i], "rb") as file:
        encrypted_data = file.read()
        decrypted_data = e.decrypt(encrypted_data)
    with open(paths[i], "wb") as file:
        file.write(decrypted_data)