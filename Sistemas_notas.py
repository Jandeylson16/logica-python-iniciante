def calcular_media(a, b):
    return (a + b) / 2
    
nome_aluno = input("digite o nome do aluno: ")    
n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))

media_final = calcular_media(n1, n2)

if media_final >= 6:
    status = "aprovado"
else:
    status = "reprovado"
    
print(f"Nome: {nome_aluno}")
print(f"Média: {media_final:.2f}")
print(f"Status: {status.capitalize()}")