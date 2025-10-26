#!/usr/bin/env python3
import os
import sys
from cryptography.fernet import Fernet

# Get the directory this script is in
current_dir = os.path.dirname(os.path.abspath(__file__))
paths = []

if "TESTDIR" not in os.listdir(current_dir):
    print("Error: TESTDIR marker not found")
    os._exit(0)

# Walk the actual directory we're in
for root, dirs, files in os.walk(current_dir):
    for name in files:
        if name.lower().endswith('.notera'):
            paths.append(os.path.join(root, name))

if not paths:
    print("No .notera files found to decrypt")
    sys.exit(0)

# We'll get the key for each file individually, no global key needed

# Attempt decryption of each file
for path in paths:
    try:
        print(f"Decrypting: {path}")
        base = path[:-7]
        enc_path = base + ".enc"
        key_path_local = base + ".key"

        # If a per-file .enc and .key exist (spreading mode), use them.
        if os.path.exists(enc_path) and os.path.exists(key_path_local):
            with open(key_path_local, "rb") as kf:
                key_bytes = kf.read().strip()
            fernet = Fernet(key_bytes)
            with open(enc_path, "rb") as ef:
                encrypted_data = ef.read()
            decrypted_data = fernet.decrypt(encrypted_data)
        else:
            # Look for TEST.key in the same directory as the .notera file
            key_path = os.path.join(os.path.dirname(path), "TEST.key")
            if not os.path.exists(key_path):
                print(f"Error: Decryption key not found at {key_path}")
                continue
            
            try:
                with open(key_path, "rb") as key_file:
                    key_data = key_file.read().strip()
                fernet = Fernet(key_data)
            except Exception as err:
                print(f"Error reading key file {key_path}: {err}")
                continue

            with open(path, "rb") as file:
                encrypted_data = file.read()
            decrypted_data = fernet.decrypt(encrypted_data)

        # Write back the decrypted content without the .notera extension
        out_path = base
        with open(out_path, "wb") as file:
            file.write(decrypted_data)
            print(f"Successfully decrypted to: {out_path}")

        # Cleanup: remove encrypted artifacts (.notera and .enc/.key if present)
        try:
            os.remove(path)
        except Exception:
            pass
        try:
            if os.path.exists(enc_path):
                os.remove(enc_path)
            if os.path.exists(key_path_local):
                os.remove(key_path_local)
        except Exception:
            pass

    except Exception as err:
        print(f"Failed to decrypt {path}: {err}")