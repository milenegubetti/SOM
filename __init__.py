from compactar import compactar
from descompactar import descompactar

if __name__ == "__main__":

    print("1 - Compactar")
    print("2 - Descompactar")
    opcao = input(" : ")

    if opcao == "1":

        caminho = input("Caminho: ")
        imagem = input("Nome: ")
        try:
            nome, formato = imagem.split(".")
        except ValueError:
            exit()

        compactar(caminho, nome, formato)

    elif opcao == "2":

        caminho = input("Caminho: ")
        imagem = input("Nome: ")
        try:
            nome, formato = imagem.split(".")
        except ValueError:
            exit()

        descompactar(caminho, nome, formato)

    else:

        exit()
