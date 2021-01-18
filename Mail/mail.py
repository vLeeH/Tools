import smtplib
import os 
from email.message import EmailMessage
import imghdr  
from time import sleep
import getpass

# github.com/vLeeH - 2021
# Disable the less secure apps in your account.

# Credentials
send_email = "EMAIL_THAT_WILL_SEND"
rec_email = "EMAIL_TO_RECEIVED"
password = input(str('Enter your password: '))

# Computer Info
username = getpass.getuser()

# Info
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
            <h1 style="color: gray;">Click in the image down below ↙</h1>
        </body>
    </html>
''', subtype='html')

# Files
files= ['image.jpg']
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