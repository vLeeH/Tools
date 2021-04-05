# github.com/vLeeH - 2021

import os
try:
    from pyrastreio import correios
except ImportError:
    os.system("pip install pyrastreio")

print('-='*25)
print("THIS PROGRAM WORKS ONLY FOR TRACKING ORDERS OF CARRIERS [SEDEX, MAILS]!")

while True:
    # Get the code of the order
    code = str(input("TRACKING CODE: "))
    resu = correios(code)
    try:
        print(f'{resu[0]["data"]} | {resu[0]["hora"]} | {resu[0]["mensagem"]}')
    except Exception as e:
        print(f"[ERROR]The code did not work please try again! \n {e}")

    try: 
        for i in range(1, 6):
            try:
                print(f'{resu[i]["data"]} | {resu[1]["hora"]} | {resu[i]["mensagem"]}')
            except:
                pass
    
    except Exception as e: 
        print(f'[ERROR] {e}')

# https://github.com/vLeeH/ToolsPy/edit/main/Track/track.py
