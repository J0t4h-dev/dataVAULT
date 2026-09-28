from time import sleep
from os import system

# ====================== > > LISTAS < < ============================

opc_produtos = {
    "CADASTRAR PRODUTO": "CADASTRAR PRODUTO",
    "LISTAR PRODUTOS": "LISTAR PRODUTOS",
    "VOLTAR AO MENU": "VOLTAR AO MENU",
}

opc_principal = {"PRODUTOS": "PRODUTOS", "SAIR": "SAIR"}


# ==================================================================
# ==================================================================


def linha(tamanho=42):
    """
    -> Escreve uma linha personalisavel
    :param tamanho: Tamanho da linha a ser escrita(opcional)
    """

    print("=" * tamanho)


# ==================================================================
# ==================================================================


def cabecalho(título):
    """
    -> Escreve um cabecalho entre 2 linhas
    :param título: Texto que será escrito dentro do cabeçalho
    """

    linha()
    print(título.center(42))
    linha()


# ==================================================================
# ==================================================================


def menu(título, opcoes):
    """
    -> Escreve um título com opções personalisaveis
    :param título: Texto que irá aparecer no cabeçalho do menu
    :param opcoes: Lista das opções a serem escritas, organizadas por
    uma sequência de 1 à n
    :return: Retorna um número inteiro
    """

    cabecalho(título)
    c = 1
    for v in opcoes.values():
        print(f"[{c}] {v}")
        c += 1
    linha()
    r = int(input("\nSua opção: "))
    clear()
    return r


# ==================================================================
# ==================================================================


def sair():
    """
    -> Usado para sair do programa principal com elegância
    """
    clear()
    etc = "."
    for c in range(3):
        print(f"SAINDO DO PROGRAMA{etc}")
        etc += "."
        sleep(1)
        system("cls")
    print("\033[31mPROGRAMA ENCERRADO\033[m")


# ==================================================================
# ==================================================================


def clear():
    """
    -> Apaga todo o conteúdo em exibição na tela
    """

    system("cls")


# ==================================================================
# ==================================================================


def VALOR_N_EXISTE():
    input("Valor inválido, pressione Enter para tentar novamente...")
    clear()
