import requests
import simplejson
import json
import os, sys 


################################## resultado deseado #############################
secuencia = []

def calculo(numero):
	del secuencia[:]
	entrada = numero
	if isinstance(numero, int):
		while numero != 1:
			if (numero % 2 == 0):
				numero = numero / 2
			else:
				numero = (numero * 3) + 1

			secuencia.append(numero)

		json_data = {
	
		}
		json_data['secuencia'] = secuencia
		json_data['numero'] = str(entrada)

	else:
		json_data = {
	
		}
		json_data['numero'] = " "

	resultado = json_data
	return resultado


###########################################################
valores = [30, 'e23',13, 20, " ", 17, "5g5g5g5g5", 45, "1w1111", 24]
i = 0
mostrar = []
lista = []
lista2 = []

for i in valores:
    r = requests.get('http://localhost/calculoSecuenciaCollatz.php?numero='+str(i))

    valor = str(i)
    
    if isinstance(i, int):
    	validez = '1'
    else:
    	validez = '0'
	
    esperado = calculo(i)
    esperado = json.dumps(esperado)

    generados = json.dumps(r.json())

    if esperado == generados:
    	status = "1"
    else:
    	status = "0"

    datos = {'valor' : valor, 'secuencia' : generados, 'status' : status, 'validez' : validez}
    lista.append(datos) 

    mostrar = [valor, status, validez, generados]
    lista2.append(mostrar) 

#############################################################################################
print("RESULTADO DEL TEST")
Tabla = """\
+----------------------------------------------------------------------------------------------------------------------------+
| NUM            STATUS      PASS                                SECUENCIA                                                   |
|----------------------------------------------------------------------------------------------------------------------------|
{}
+---------------------------------------------------------------------------------------------------------------------------+\
"""

Tabla = (Tabla.format('\n'.join("| {:<16} {:<10} {:<10} {:>8} ".format(*fila)
for fila in lista2)))
print (Tabla)   
	

############################################ Guardar archivo json ############################

ruta = "C:/secuenciaCollatz/"

if not os.path.exists(ruta):
  os.makedirs(ruta)

with open(ruta+str('secuencia.txt'), 'w') as outfile:
	json.dump(lista, outfile)

######################################################### NOTA ###################################
print('NOTA')
print ('la bateria de pruebas se realizo con 10 valores de entrada, se espera que 6 valores pasen, el reporte contiene:')
print( ' 1- El numero ingresado = valor')
print (' 2- El estatus de los resultados, la comparacion con lo esperado y lo generado, 1 si son iguales, 0 si no son iguales')
print (' 3- si el valor ingresado paso o no paso')
print (' 4- La secuencia generada por el test')
print('se genero un json en la ruta C:/secuenciaCollatz/')



