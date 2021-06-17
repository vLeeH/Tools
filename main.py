# -*- coding: utf-8 -*-

try: 
    import os 
    import imghdr  
    from time import sleep
    import getpass
    import socket
    import platform
    import smtplib
    from email.message import EmailMessage
    import sys
except ImportError as i: 
    print(f"{i}") 
else: 
    os.system('python packages/MailBrute.py')
