#CONVERSOR DE MEDIDAS
print("CONVERSOR DE DISTANCIAS")
entrada = float(input("Digite uma distancia em metros: "))

km = entrada / 1000
hm = entrada / 100
dam = entrada / 10
dm = entrada * 10
cm = entrada * 100
mm = entrada * 1000

print("{:.3} km \n{:.3} hm \n{:.3} dam \n{:.3} dm \n{} cm \n{} mm ".format(km, hm, dam, dm, cm, mm))