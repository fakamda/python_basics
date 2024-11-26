#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso = 1.5

#crudo
crudo_promedio = 5
mi_crudo = 3.5

#dif de duracion
diferencia_con_min = 100 - curso / otros_cursos_min * 100  #promedio
diferencia_con_max = 100 - curso * 1000 // otros_cursos_max / 10 # otra manera de sacar el promedio
diferencia_con_promedio = 100 - curso / otros_cursos_promedio * 100

#calculando el porcentaje d etiempo vacio
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_curso = 100 - curso * 1000 // mi_crudo / 10

print(f'El curso nuestro dura un {diferencia_con_min}% menos que el mas rapido')
print(f'El curso nuestro dura un {diferencia_con_max}% menos que el mas rapido')
print(f'El curso nuestro dura un {diferencia_con_promedio}% menos que el mas rapido')

print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimino el {tiempo_vacio_curso}% de tiempo vacio')

#mostrando dif si los cursos duraran 10 horas

print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // curso / 10} horas de otros cursos')