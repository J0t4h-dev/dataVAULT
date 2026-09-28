from src.interface import *

# ==================================================================
# ==================================================================


def LER_PRODUTO(arq):
    cabecalho(opc_produtos["LISTAR PRODUTOS"])
    print(
        f"{'ID':>4}|{'NOME':<20}|{'TIPO':<12}|{'VALOR':>10}|{'ESTOQUE':>10}|{'ESTOQUE MÍNIMO':>15}"
    )
    with open(arq, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dado = linha.strip().split(";")
            print(
                f"{dado[0]:>4}|{dado[1]:<20}|{dado[2]:<12}|{dado[3].replace('.', ','):>10}|{dado[4]:>10}|{dado[5]:>15}"
            )
    input("\n[Enter] para voltar...")
    clear()


# ==================================================================
# ==================================================================


def AD_PRODUTO(arq):
    with open(arq, "a+", encoding="utf-8") as arquivo:
        cabecalho(opc_produtos["CADASTRAR PRODUTO"])
        nome = str(input("NOME: "))
        tipo = str(input("TIPO: "))
        valor = str(input("VALOR: R$").replace(",", "."))
        estoque = int(input("ESTOQUE ATUAL: "))
        estoque_min = int(input("ESTOQUE MÍNIMO: "))
        clear()
        id_produto = id_auto(arq)
        arquivo.write(
            f"{int(id_produto)};{str(nome)};{str(tipo)};R${float(valor):.2f};{str(estoque)};{str(estoque_min)}\n"
        )
    clear()


# ==================================================================
# ==================================================================


def arquivoCRIAR(arq):
    try:
        open(arq, "r")
    except FileNotFoundError:
        with open(arq, "x") as arquivo:
            print(f"{arq} foi criado!")
    else:
        print(f"O arquivo {arq} já existe!")


# ==================================================================
# ==================================================================


def id_auto(arq):
    with open(arq, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        id_s = list()
        for linha in linhas:
            dado = linha.strip().split(";")
            id_s.append(int(dado[0]))
        if len(id_s) == 0:
            id = 1
        else:
            id = max(id_s) + 1
        return id
