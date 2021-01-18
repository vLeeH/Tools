import smtplib
import os 
from email.message import EmailMessage
import imghdr  
from time import sleep
import getpass
import socket
import platform

# github.com/vLeeH - 2021
# Disable the less secure apps in your account.

# Credentials
send_email = "EMAIL_THAT_SEND_EMAIL"
rec_email = "EMAIL_RECEIVE"
password = input(str('Enter your password: '))

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
msg.add_alternative(f'''
    <!DOCTYPE html>
    <html lang="en">
        <body>
            <h1 style="color: gray;">See the image and the Computer Informations ↙</h1>
            <h2>The computer informations:</h2><br>
            {inf}
        </body>
    </html>
''', subtype='html')

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
        print(f'[ERROR] {e}')

# Send the email
try: 
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: 
        smtp.login(send_email, password)
        print(f'Login in the email {send_email}')
        sleep(1)
        smtp.send_message(msg)
        print(f'\033[1;32m Email has been sent to {rec_email}')

except Exception as e: 
    print(f'[ERROR] {e}')

# https://github.com/vLeeH/ToolsPy/blob/main/ToolsPy/mail.py
