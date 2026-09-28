# ==================================================================
# ==================================================================


def LER_PRODUTO(arq):
    print(
        f"{'ID':>4}|{'NOME':<20}|{'TIPO':<12}|{'VALOR':>10}|{'ESTOQUE':>10}|{'ESTOQUE MÍNIMO':>15}"
    )
    with open(formatTXT(arq), "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dado = linha.strip().split(";")
            print(
                f"{dado[0]:>4}|{dado[1]:<20}|{dado[2]:<12}|{dado[3].replace('.', ','):>10}|{dado[4]:>10}|{dado[5]:>15}"
            )


# ==================================================================
# ==================================================================


def AD_PRODUTO(arq, nome, tipo, valor, estoque, estoque_min):
    with open(formatTXT(arq), "a+", encoding="utf-8") as arquivo:
        id = id_auto(arq)
        arquivo.write(f"{id};{nome};{tipo};R${valor:.2f};{estoque};{estoque_min}\n")


# ==================================================================
# ==================================================================


def arquivoCRIAR(arq):
    try:
        open(formatTXT(arq), "r")
    except FileNotFoundError:
        with open(formatTXT(arq), "x") as arquivo:
            print(f"{formatTXT(arq)} foi criado!")
    else:
        print(f"O arquivo {formatTXT(arq)} já existe!")


# ==================================================================
# ==================================================================


def formatTXT(arq):
    return f"{arq}.txt"


# ==================================================================
# ==================================================================


def id_auto(arq):
    with open(formatTXT(arq), "r", encoding="utf-8") as arquivo:
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
