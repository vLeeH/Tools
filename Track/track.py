import os
try:
    from pyrastreio import correios
except ImportError:
    os.system("pip install pyrastreio")

print("!!!ATTENTION THIS PROGRAM WORKS ONLY FOR TRACKING ORDERS OF CARRIERS [SEDEX, MAILS]!!!")
while True:
    intt = str(input("TRACKING CODE: "))
    res = correios(intt)
    try:
        print(f'{res[0]["data"]} | {res[0]["hora"]} | {res[0]["mensagem"]}')
    except:
        print("The code did not work please try again!")

    for i in range(1, 6):
        try:
            print(f'{res[i]["data"]} | {res[1]["hora"]} | {res[i]["mensagem"]}')
        except:
            pass

