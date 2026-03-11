pontos = {}

for i in range(5):
    nome = input("Digite o nome do jogador: ")
    pontuacao = float(input("Digite a quantidade de pontos inicias do jogador: "))

    pontos[nome] = pontuacao

nome_jogador = input("\nVerificar jogadores: ")
pontos_conquistados = float(input("Informe os pontos conquistados: "))

if nome_jogador in pontos:
    pontos[nome_jogador] = pontos[nome] + pontos_conquistados
    print("Jogador encontrado")

else:
    print("Jogador não encontrado")

    
    for jogador, pontuacao in pontos.items():
        print(f"{jogador} |{pontuacao}")
        