nombres = ["facundo", "juan", "ruperto", "ekko", "nose"]
apellidos = ["dominguez", "lopez", "ruperstinsky", "time", "eson"]

with open("problems\\nombres_apellidos.txt", "w") as archivos:
    archivos.writelines("Los datos son:\n\n")
    # [archivos.writelines(f"Nombre: {n} \n Apellido: {a} \n-----\n") for n,a in zip(nombres,apellidos)] #para hacerlo dentro de una linea hacemos una lista
    for n,a in zip(nombres, apellidos):
        archivos.writelines(f"Nombre: {n} \n Apellido: {a} \n-----\n")