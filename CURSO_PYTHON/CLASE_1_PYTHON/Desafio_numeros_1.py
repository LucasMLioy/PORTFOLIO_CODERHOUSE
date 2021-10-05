#Crear un programa para calcular la nota final de un alumno en base a dos exámenes, los exámenes cuentan con un 
#porcentaje distinto de la nota final
#nota_1  cuenta como el 40% de la nota final
#nota_2 cuenta como el 60% de la nota final

print("Bienvenido al campus virtual. El sistema le pedirá que ingrese dos notas y calculará su promedio final. Recuerde que la nota 1 cuenta como el 40% de la nota final, mientras que la nota 2 cuenta como el 60% de la nota final\n") 
nota1=int(input(f"Ingrese la primera nota: "))
nota2=int(input(f"Ingrese la segunda nota: "))

nota_final=(nota1*0.4) + (nota2*0.6)

print(f"Su nota final es igual a: {nota_final}")
