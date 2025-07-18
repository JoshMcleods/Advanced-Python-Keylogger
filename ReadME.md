This project is created solely for **educational and research purposes** to help users understand how keyloggers work, the potential security risks, and how to defend against such threats.

**Important:**

- Do **NOT** use this software to capture data without explicit permission from all parties involved.  
- Unauthorized use of keylogging software may be illegal and punishable by law.  
- The author is **NOT responsible** for any misuse or damage caused by this code.

Use this project ethically, responsibly, and always respect privacy and legal boundaries.

## Project and Research Notes

## Dependancies 
- `pynput` listens to keyboard input 
- `sounddevice` - captures mic audio 
- `cryptography` - used for encrypting log files
- `requests` - to send IP info to remote server
- `Pillow` - used to get screenshots
- `pyperclip` - clipboard access (for Windows use pywin32)
Use pip install ""

## Standard Libary 

| Library/Module          | Purpose                                         |
|-------------------------|-------------------------------------------------|
| `email.mime.multipart`  | Create email message containers for attachments |
| `email.mime.text`       | Add plain text to emails                        |
| `email.mime.base`       | Attach binary files (e.g., .txt, .jpg)          |
| `email.encoders`        | Encode attachments (base64)                     |
| `smtplib`               | Send email via SMTP server (e.g., Gmail)        |
| `socket`                | Get system IP address or hostname               |
| `platform`              | Detect OS and system info                       |
| `time`                  | Add delays or timestamps                        |
| `os`                    | File system access, path manipulation, system commands |
| `getpass`               | Securely retrieve the username or passwords     |
| `multiprocessing`       | Run multiple processes in parallel              |

## Third-Party Libraries

| Libraries / Modules         | Purpose                                  |
|-----------------------------|------------------------------------------|
| `pynput`                    | Listen to keyboard input (keylogging)    |
| `scipy.io.wavfile`          | Save audio input to `.wav` files         |
| `sounddevice`               | Capture microphone audio                 |
| `cryptography.fernet`       | Symmetric encryption of data or logs     |
| `requests`                  | Send HTTP requests (e.g., IP tracker)    |
| `PIL.ImageGrab`             | Capture screenshots (part of Pillow)     |


By default google blocks the s.login() function through python for security reasons, so inorder to login you do not use your actual password instead you must generate an app password after turning on 2 step verification where google will provide you a 16 letter randomised password, it is also recommended to use a disposable email account.

Getting the public ip address using ipify.org has a max query per user, after the max query is reached an exception will occur saying it could not retreive the Public IP addresss.

For the audio capture, channel 2 is a common default although if it does not capture audio input it could be due to the wrong input capture, so adding the d.default.device = (2, None) line can fix channel errors. Otherwise, the audio channels are printed to system info.txt and you can decide which audio device to capture from. If you would like to capture a longer .wav audio file changing the seconds is optional.

If you do not encrypt the files before sending them your message will be automatically blocked by google as they present potential security issues.

If you want to obfuscate simply change file names, but for educational purposes this makes it clearer

Decryption is intended to be done on your side after receiving the encrypted emails, and will need to replace encrypted_files values with emailed files names.
