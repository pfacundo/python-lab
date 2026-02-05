
gas1311=327.67
gas1112=868.60
aguaNov=2070
aguaDic=1653.30
aguaEne=1327.37
aguatotal=aguaNov + aguaDic + aguaEne
depa=17000
gas1311diario=gas1311/28
gas1112diario=gas1112/29
gasNovnosotros=gas1311diario*11
nosotrosgas=gas1112/5
gasPropietario=gas1311 - (gas1311diario*11)

print(f"Gasto de gas noviembre : {gas1311} pagado (sacar del alquiler) medido al 11/12\
\nde los cuales solo nos corresponde pagar 11 dias : {(gasNovnosotros):.2f}\
\nGasto de gas diciembre : {gas1112} por pagar gas propietario {gasPropietario:.2f}\
#\nDe esos {gas1311} nosotros pagamos 11 dias ({(gas1311diario*11):.2f})y el \
#\npropietario 17 dias ({(gasPropietario):.2f})"
)

print(f"Gastos de gas por cada uno a pagar de dic (5): ${nosotrosgas}")
print(f"Gastos de gas por cada uno a pagar de nov (5): ${gasNovnosotros/5:.2f}")


aguaDicEne=aguaDic + aguaEne
nosotrosagua=aguaDicEne/5 
print(f"El agua de Noviembre es: {aguaNov} que esta calculado hasta el 25/11\
      \nEl agua de Diciembre es {aguaDic} y enero es {aguaEne} = {aguaDicEne} que seria lo que nos corresponde pagar \
      \nCada uno debe pagar de agua (dic y ene): {nosotrosagua} \
      \ntotal de agua: {aguatotal}")
depaFinal=depa - aguaNov - gas1311
print(f"Al pagar el monto de las cuentas de noviembre de agua ({aguaNov}) y gas ({gas1311}), \
\ndebemos restarle al monto del alquiler {depa} - {aguaNov} - {gas1311} = {depaFinal} \n\
que seria el monto final del alquiler a pagar.")
depaCadaUno=depaFinal/4
print(f"El monto final del alquiler a pagar por cada uno es: {depaCadaUno}\
      \nEl gasto total por cada uno (alquiler + gas + agua) es: {depaCadaUno + nosotrosgas + (aguatotal/5):.2f}")
