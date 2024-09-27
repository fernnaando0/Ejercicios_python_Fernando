from ejercicios import *

#Ejercicio 1
def test_calcula_imc()->float:
  peso=66.1
  altura=1.78
  imc=calcula_imc(peso,altura)
  print("Para una altura de ",altura," y un peso de ",peso," el IMC es: ",imc)
  

#Ejercicio 2
def test_calcula_estado_nutricional()->str:
  peso=66.1
  altura=1.78
  imc=calcula_imc(peso,altura)
  res=calcula_estado_nutricional(peso,altura)
  print("Para una altura de ",altura," y peso ",peso," el IMC es: ",imc,".El estado nutricional es:" ,res)


#Ejercicio 3
def test_trata_estados_nutricionales()->None:
  datos = [
    Datos_nutricionales(60.0, 1.6),
    Datos_nutricionales(75.4, 1.75),
    Datos_nutricionales(87.9, 1.69),
    Datos_nutricionales(45.1, 1.65)]
  lista_resultado=trata_estados_nutricionales(datos)
  for i, resultado in enumerate(lista_resultado):
    peso=datos[i].peso
    estatura=datos[i].estatura
    imc=resultado[0]
    estado_nutricional=resultado[1]
    print(f"Para (peso:{peso},altura:{estatura}) el IMC es: {imc:.2f} y el estado nutricional es: {estado_nutricional}")
 
  
#Ejercicio 4
def test_producto_escalar()->None:
  vector_a1 = [2, 3, 1]
  vector_a2 = [3, 4, 7]
  resultado_a = producto_escalar(vector_a1, vector_a2)
  vector_b1 = [2,3]
  vector_b2 = [3,4,7]
  resultado_b = producto_escalar(vector_b1, vector_b2)
  print(f"El producto escalar de {vector_a1} y {vector_a2} es: {resultado_a}")
  print(f"El producto escalar de {vector_b1} y {vector_b2} es: {resultado_b}")

  
#Ejercicio 5
def test_calcula_promedio_edades_sexo()->None:
  edades=[Edad(23,'M'),
	Edad(30,'M'),
	Edad(56,'H'),
	Edad(18,'H'),
	Edad(34,'M'),
	Edad(7,'M'),
	Edad(95,'H'),
	Edad(37,'M'),
	Edad(36,'H')]
  promedio_hombres=calcula_promedio_edades_sexo(edades,"H")
  print(f"El promedio de edad de los hombres es {promedio_hombres}")
  promedio_mujeres=calcula_promedio_edades_sexo(edades,"M")
  print(f"El promedio de edad de los hombres es {promedio_mujeres}")
  promedio_error=calcula_promedio_edades_sexo(edades,"J")
  print(f"El promedio de edad de los J es {promedio_error}")
        
#El programa empieza a ejecutarse por aquí
if __name__=='__main__':
  test_calcula_imc()
  test_calcula_estado_nutricional()
  test_trata_estados_nutricionales()
  test_producto_escalar()
  test_calcula_promedio_edades_sexo()