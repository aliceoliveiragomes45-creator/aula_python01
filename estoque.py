#CRIACAO DO DIVIONÁIO ESTOQUE
estoque = {
    "camisa":50,
    "calça":15,
    "bone":30,
    "tenis naique":25,
}
#MOSTRAR ESTOQUE ATUAL
print("Estoque atual: ")
for produto, quantidade in estoque.items():
    print(f"{produto}  : {quantidade}")
    #PEDINDO DADOS PARA O USUARIO DO SISTEMA
    nome_produto = input("\ninforme o nome do produto vendido: ")
    quantidade_vendida = int(input("\ninforme a quantidade vendida:"))

#ATUALIZAR O ESTOQUE
if nome_produto in estoque:
    if quantidade_vendida <= estoque[nome_produto]: 
        estoque[nome_produto] = estoque[nome_produto] = quantidade_vendida
        print("Venda Realizada com sucesso")
else:
    print("Produto não encontrado")
 #MOSTRAR ESTOQUE ATUALIZADO
    for produto, quantidade in estoque.items():
       print(f"{produto} | {quantidade}")      
