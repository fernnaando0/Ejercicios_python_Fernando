from typing import NamedTuple, List, Tuple

#EJERCICIO 1
def calcula_imc(peso:float,altura:float)->float:
    imc=round(peso/(altura*altura),2)
    return imc


#EJERCICIO 2
def calcula_estado_nutricional(peso:float,altura:float)->str:
    imc=calcula_imc(peso,altura)
    if imc < 18.5:
            res=("bajo peso")
    elif 18.5 <= imc < 25:
            res=("peso saludable")
    elif 25 <= imc <= 30:
            res=("sobrepeso")
    else:
            res=("obesidad")
    return res

#EJERCICIO 3
Datos_nutricionales=NamedTuple("dn",[("peso",float),("estatura",float)])
def trata_estados_nutricionales(Fernando:list[Datos_nutricionales])->list[tuple]:
    res=list()
    for elemento in Fernando:
        imc = calcula_imc(elemento.peso,elemento.estatura)
        en = calcula_estado_nutricional(elemento.peso,elemento.estatura)
        tupla=(imc,en)
        res.append(tupla)
    return res

#EJERCICICIO 4
def producto_escalar(vector1:list[int],vector2:list[int])->int:
        if len(vector1) != len(vector2):
                return None
        
        producto = sum(x * y for x, y in zip(vector1,vector2))
        return producto

#EJERCICIO 5
class Edad(NamedTuple):
        edad:int
        sexo:str
def calcula_promedio_edades_sexo(lista_edades:list[Edad],sexo:str)->float:
        edades_filtradas = [persona.edad for persona in lista_edades if persona.sexo == sexo]
        if len(edades_filtradas) == 0:
                return None
        else:
                promedio = sum(edades_filtradas)/ len(edades_filtradas)
                return promedio