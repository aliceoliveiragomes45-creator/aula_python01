import os

def executar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True)
    except Exception as e:
        print("Erro ao executar comando:", e)
def mostrar_data():
    executar_comando("date")

def mostrar_hora():
    executar_comando("time")

def mostrar_bloco_de_notas():
    executar_comando("notepad")

def mostrar_ip():
    host = input("ipconfig: ")
def abrir_navegador():
    executar_comando("www.google.com")
def mostrar_calculadora():
    executar_comando("calc")
def abrir_explorador_de_arquivos():
    executar_comando("explorer")
def mostrar_arquivo():
    executar_comando("dir")
def criar_pasta("")

while True:
    print("\n -------Menu comandos--------")
    print("1- Mostrar data")
    print("1- Mostrar hora")
    print("3- Abrir bloco de notas")
    print("4- Ver ip da maquína")
    print("5- Abrir navegador")
    print("6- Abrir calculadora")
    print("7- Abrir Explorador de arquivos")
    print("8- Criar uma pasta ")
    print("9- Mostrar estrutura de pastas")
    print("10- Sair")
