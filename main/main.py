# CÓDIGO PRINCIPAL

from src.interface import *
from src.produto import *

arquivos = {"PRODUTOS.txt": "PRODUTOS.txt"}

for arq in arquivos.values():
    arquivoCRIAR(arq)

while True:

    resp = menu("DATA VAULT", opc_principal)

    if resp == 1:
        while True:
            resp = menu(opc_principal["PRODUTOS"], opc_produtos)

            if resp == 1:
                AD_PRODUTO("PRODUTOS.txt")

            elif resp == 2:
                LER_PRODUTO(arquivos["PRODUTOS.txt"])

            elif resp == 3:
                break

            else:
                VALOR_N_EXISTE()
    elif resp == 2:
        sair()
        break

    else:
        VALOR_N_EXISTE()
