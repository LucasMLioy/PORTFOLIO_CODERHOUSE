

#Se tiene  una cadena de texto, pero al revés. 
#Al parecer contiene el nombre de un alumno, la nota de un exámen y la materia. 

#De forma individual, realiza lo siguiente: 

#Da vuelta la cadena y asignala a una variable llamada cadena_volteada. (Para devolver una cadena dada vuelta 
#se usa el tercer índice negativo con slicing: cadena[::-1])

#Extrae el nombre y apellido y guárdalo en una variable llamada nombre_alumno 

#Extrae la nota y guárdala en una variable llamada nota

#Extrae la materia y guárdala en una variable llamada materia 

#Mostrá por pantalla la siguiente estructura formateando las anteriores variables en una variable llamada cadena_formateada
#NOMBRE APELLIDO ha sacado un NOTA en MATERIA
#cadena = “acitametaM ,5.8 ,otipeP ordeP”

cadena='acitametaM,5.8,otipeP ordeP'

cadena_volteada= cadena[::-1] # voltea el orden de la cadena

nombre_alumno= cadena_volteada[0:12:1] # tomo nueva cadena volteada[posicion_1er_caracter:posicion_ultimo_caracter_+_1:salto]

nota= cadena_volteada[13:16:1]

materia= cadena_volteada[17:27:1]

cadena_formateada=print(f"{nombre_alumno} ha sacado un {nota} en {materia}")