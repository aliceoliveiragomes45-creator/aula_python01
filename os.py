import subprocess 
import os
def executar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True)
    except Exception as e:
        print("Erro ao executar comando:", e)
def mostrar_ip():
    executar_comando("ipconfig")

def renovar_ip():
    executar_comando("ipconfig /renew")

def mostrar_ip_completo():
    executar_comando("ipconfig /all")

def ping_host():
    host = input("Digite o IP ou HOSTNAME: ")
    executar_comando(f"ping {host}") 

def menu():
     while True:
        print("\n-----ferramenta de rede------")
        print("1- mostrar ip")
        print("2- renovar ip")
        print("3- mostrar configurações de rede completa")
        print("4- ping")
        print("0 - sair")

        print("--------- criado por Alice -----------")

        opcao = str(input("escolha: "))

        match opcao:
            case "1":
                mostrar_ip()
            case "2":
                renovar_ip()
            case "3":
                mostrar_ip_completo()
            case "4":
                ping_host()
            case "0":
                print("saindo")
                break
            case _: 
                print("eita caba sabido!")
if __name__ == "__main__":
    menu()