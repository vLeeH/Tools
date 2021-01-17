import os
try:
    from pyrastreio import correios
except ImportError:
    os.system("pip install pyrastreio")

print("!!!ATENÇÃO ESTE PROGRAMA FUNCIONA APENAS PARA RASTREIO DE ENCOMENDAS DAS TRANSPORTADORAS [SEDEX, CORREIOS]!!!")
while True:
    intt = str(input("CODIGO DE RASTREIO: "))
    res = correios(intt)
    try:
        print(f'{res[0]["data"]} | {res[0]["hora"]} | {res[0]["mensagem"]}')
    except:
        print("o codigo não funcionou tente novamente!")

    for i in range(1, 6):
        try:
            print(f'{res[i]["data"]} | {res[1]["hora"]} | {res[i]["mensagem"]}')
        except:
            pass

