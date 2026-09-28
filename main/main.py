# CÓDIGO PRINCIPAL

from src.interface import *
from src.produto import *

arquivos = {"arqPRODUTOS": "PRODUTOS"}

for arq in opc_principal:
    if arq != opc_principal[-1]:
        arquivoCRIAR(arq)

while True:

    resp = menu("DATA VAULT", opc_principal)
    clear()

    if resp == 1:
        while True:
            resp = menu(opc_principal[1 - 1], opc_produtos)
            clear()

            if resp == 1:
                cabecalho(opc_produtos[resp - 1])
                nome = str(input("NOME: "))
                tipo = str(input("TIPO: "))
                valor = str(input("VALOR: R$").replace(",", "."))
                estoque = int(input("ESTOQUE ATUAL: "))
                estoque_min = int(input("ESTOQUE MÍNIMO: "))
                AD_PRODUTO(
                    arquivos["arqPRODUTOS"],
                    nome,
                    tipo,
                    float(valor),
                    estoque,
                    estoque_min,
                )
                clear()
            elif resp == 2:
                cabecalho(opc_produtos[resp - 1])
                LER_PRODUTO(arquivos["arqPRODUTOS"])
                input("\n[Enter] para voltar...")
                clear()
            elif resp == 3:
                break
            else:
                input("Valor inválido, pressione Enter para tentar novamente...")
                clear()

    elif resp == 2:
        clear()
        sair()
        break

    else:
        input("Valor inválido, pressione Enter para tentar novamente...")
