km_inicial = int(input("Informe seu KM inicial: "))
km_final = int(input("Informe seu KM final: "))
litros = float(input("Informe o total de litros gastos: "))

km_total = km_final - km_inicial
media = km_total - litros
print("Foram gastos, %.f litros" % media)
