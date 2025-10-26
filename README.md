NOTERA
---------------------------------------------
This is Notera, a simple window_os-native python ransomware without ransom :).
It's very good and quick, devastating too. Even though it's still not system-wide complete, the result is quite promising
The only noteable problem is subprocess.run(["python", os.path.join(folders[i], os.path.basename(__file__))]), on line 96 of notera.py, which doesn't run if python is not on path or not ran as python(some run as python3 or else). Edit them by your uses and target.
Educational Disclaimer : Hacking other people's devices is illegal without permission of the owners. The author is not responsible for any illegal action caused by uses of this piece of software.
----------------------------------------------
Feautures:
-Testmode _ Trigger by creating an empty, extension-less file named TESTDIR
    |Uses reversable encryption(Key is in TEST.key, automatic decryption avaliable in
    Decryptiontest.py).
