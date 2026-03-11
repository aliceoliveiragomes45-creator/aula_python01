pessoa_1={"arroz","feijao","acucar","macarrao"}
pessoa_2={"arroz","batata","leite","cafe"}
pessoa_3={"macarrao","arroz","feijao"}
pessoa_4={"feijao","acucar","leite","arroz"}

cliente1= set(pessoa_1)
cliente2= set(pessoa_2)
cliente3= set(pessoa_3)
cliente4=set (pessoa_4)

print(f"A lista de compras do cliente1 e:{pessoa_1}")
print(f"A lista de compras do cliente2 e:{pessoa_2}")
print(f"A lista de compras do cliente3 e:{pessoa_3}")
print(f"A lista de compras do cliente4 e:{pessoa_4}")

itens_essenciais=pessoa_1.intersection(pessoa_2,pessoa_3,pessoa_4)
print("Itens essenciais (todos tem em comum):")
print(itens_essenciais)

itens_totais= pessoa_1 .union (pessoa_2,pessoa_3,pessoa_4)

print("\ntodos os itens sem repetir:")
print(itens_totais)

print("Quantidade total de itens diferentes:")
print(len(itens_totais))


todos_itens=list(pessoa_1) + list(pessoa_2) +list(pessoa_3) +list(pessoa_4)
itens_unicos={item for item in todos_itens if todos_itens.count(item)==1}
 
print("itens que nao se repetem:",itens_unicos)