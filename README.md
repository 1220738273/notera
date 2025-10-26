# Notera

A Python-based file encryption tool designed for educational purposes and security research. This project demonstrates basic encryption techniques and file system operations in Python.

## ⚠️ Educational Disclaimer

This software is created for **educational purposes only**. It is designed to demonstrate encryption concepts and file system manipulation. Any use of this software for malicious purposes or without explicit permission is strictly prohibited. The author assumes no liability for any misuse of this software.

## 🔑 Features

- **Test Mode**: A safe environment for testing encryption functionality
  - Activated by creating an empty file named `TESTDIR`
  - Uses reversible encryption with `TEST.key`
  - Includes automatic decryption via `Decryptortest.py`
- **Killswitch**: To exclude folders from being encrypted
  - Activated by creating an empty file named `PREFC`
  - Kill `notera.py` with `os._exit(0)` as it starts
- **Cross-Platform Support**: Not yet. Only windows. May work on others if you edit line 23 in `notera.py`
- **Fast and Efficient**: Quick file processing and encryption
- **Recursive Operation**: Can process files in nested directories

## 🛠️ Technical Notes

- The tool uses the `cryptography.fernet` module for secure encryption
- Default configuration uses Python's standard file system operations
- For Python path configuration, modify the command in `notera.py` line 96:
  ```python
  subprocess.run(["python", os.path.join(folders[i], os.path.basename(__file__))])
  ```
  Adjust `"python"` to match your system's Python command (e.g., `"python3"`)

## 📝 Usage

1. Create an empty file named `TESTDIR` in the target directory to enable test mode
2. Run `notera.py` to encrypt files
3. Use `Decryptortest.py` to decrypt files in test mode

## 🔒 Security

- Always run in test mode first
- Keep encryption keys secure
- Only use on systems you have permission to access

## ⚖️ License

See the [LICENSE](LICENSE) file for details.
