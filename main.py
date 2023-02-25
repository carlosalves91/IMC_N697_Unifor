# CÁLCULO DO IMC - ÍNDICE DE MASSA CORPORAL

altura = float(input("Insira a sua altura em metros: "))
peso = float(input("Insira o seu peso em quilogramas: "))

IMC = peso / (altura ** 2)
IMCinteiro = int(IMC)

print("Seu IMC é igual a: ", IMCinteiro)