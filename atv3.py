with open("frutas.txt", "a") as arquivo:
    arquivo.write("banana\n")
    arquivo.write("pera\n")
    
print("futas adicionadas com um belo sucesso!")
with open("frutas.txt", "r") as arquivo:
    print("\nconteudo atualizado do arquivo:")
    print(arquivo.read())