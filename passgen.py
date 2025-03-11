import string
import random

while True:

    try:
        longitud = int(input("Introduce el tamaño de la contraseña (min 8 caracteres): "))
        if longitud < 8:
            print("La contraseña debe ser minimo de 8 caracteres")
        else:
            break
    except ValueError:
            longitud = int(input("Introduce un numero entero válido (min 8 caracteres):"))
            if longitud < 8:
                print("La contraseña debe ser minimo de 8 caracteres")
            else:
                break

caracteres = string.ascii_letters + string.digits + string.punctuation
contrasena = "".join(random.choice(caracteres) for i in range(longitud))
print("La contraseña generada és: "+ contrasena)