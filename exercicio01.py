valor_para_abastecer = float(input("Quanto você deseja abastecer: "))
valor_do_preco_da_gasolina = float(input("Qual o valor de cada litro de gasolina: "))

valor_calculado = valor_do_preco_da_gasolina / valor_para_abastecer 
print("Você obterá, %2.f litros de gasolina!" % (valor_calculado))
