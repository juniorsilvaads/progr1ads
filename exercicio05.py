original = float(input("Qual o valor da divida: "))
atraso = int(input("Quantos dias de atraso: "))
multa = float(input("Valor da multa por dias de atraso: "))

cal = multa * atraso
valor_dias_atraso = cal + original
print("Seu valor a pagar será %.0f" % valor_dias_atraso)
