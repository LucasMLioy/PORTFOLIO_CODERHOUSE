#Crear un programa para calcular la nota final del estudiante en base a dos exámenes, los exámenes cuentan 
#con un porcentaje distinto de la nota final
#nota_1  cuenta como el 40% de la nota final
#nota_2 cuenta como el 60% de la nota final
#>>Aspectos a incluir en el entregable:
#Tener en cuenta los temas vistos en la clase 1: números, print, input, variables, operaciones matemáticas, cadena de texto. 

print("Bienvenido, Lucas, al campus virtual. El sistema le pedirá que ingrese dos notas numéricas (entre 1 y 10) y calculará su promedio final. Recuerde que la primera nota ingresada cuenta como el 40% de la nota final, mientras que la segunda cuenta como el 60% de la nota final\n") 
estudiante= 'Lucas'
nota1=int(input(f"Ingrese la primera nota: "))
nota2=int(input(f"Ingrese la segunda nota: "))

nota_final=(nota1*0.4) + (nota2*0.6)

print(f"La nota final de {estudiante[0:5:1]} es igual a: {nota_final}")

if nota_final >=7:
    print(f"Como la nota final es igual o mayor a 7, el estudiante {estudiante[0:5:1]} ha promocionado la materia. ¡Felicitaciones!")
elif nota_final>=4 and nota_final<7:
    print(f"Como la nota final es mayor o igual a 4 y menor a 7, el estudiante {estudiante[0:5:1]} ha regularizado la materia. ¡Estudie mucho para el examen final!")
else:
    print(f"Como la nota final es menor a 4, el estudiante {estudiante[0:5:1]} ha desaprobado la materia. Por ello, debe recursar dicho espacio curricular")

