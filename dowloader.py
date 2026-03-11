import json
import os

ARQUIVO = "notas.json" 

def carregar_notas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return[]
def salvar_notas(notas):
    with open(ARQUIVO, "w") as f:
        json.dump(notas, f, indent=4)

def adicionar_notas():
    titulo = str(input("Titulo da nota: "))
    conteudo =str(input("Conteúdo de notas: "))


    notas = carregar_notas()

    nota = {
    "Titulo": titulo,
    "Conteúdo": conteudo
}
    notas.append(nota)
    salvar_notas(notas)
    print("Nota salva com sucesso!!!")

def ler_notas():
    notas = carregar_notas()
    if not notas:
        print("Nenhuma Nota encontrada! ")
        return
    ler_notas()
    indice= int(input("Digite o numero da  nota"))
    if 0 <= indice < len(notas):
            print("\nTitulo: ", notas[indice]["Titulo"])
            print("Conteúdo: ", notas[indice]["conteúdo"])
    else:
            print("Nota invalida!")

def deletar_notas():
    notas=carregar_notas()
    if not notas:
         print("Nenhuma nota para apagar! ")
         return
    listar_notas()
    indice = int(input("Informa a nota a ser apagada: "))
    if 0 <= indice < len(notas):
        notas.pop(indice) 
        salvar_notas()
        print("Nota Apagada!")
    else:
        print("Nota Invalida!")
def menu():
     while True:
          print("\n========APP DE NOTAS==========")
          print("1- Adiconar notas")
          print("2- Listar notas")
          print("3- Ler notas")
          print("4- Excluir  notas")
          print("5- Sair")
          opcao= str(input("Escolha uma opção: "))
          match opcao:
               case"1":
                    adicionar_notas()
               case"2":
                    listar_notas()
               case"3":
                    ler_notas()
               case"4":
                    deletar_notas     


