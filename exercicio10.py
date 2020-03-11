valor_salario = float(input("Informe o valor do seu salário: "))
perc_reajuste = float(input("Informe o valor percentual do reajuste: "))

cal = valor_salario + (valor_salario * perc_reajuste / 100)
print("Valor do salário mais o reajuste é, R$", cal)
