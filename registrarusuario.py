#REGISTRO DE USUARIO.
def registrarUsuario():
    continuar = 's'
    
    while continuar == 's':
        try:
            print("========= REGISTRO DE USUARIOS =======")
            
            nombre = input("INGRESE SU NOMBRE: ").strip()
            correo = input("INGRESE SU EMAIL: ").strip()
            edad = input("INGRESE SU EDAD: ").strip()
            tipoId = input("INGRESE SU TIPO DE ID: ").strip()
            numId = input("INGRESE SU NUMERO DE IDENTIFICACION: ").strip()
            
            
            if "@" not in correo or "." not in correo:
                print("EL CORREO ELECTRONICO NO ES VALIDO.")
                continue
            
    
            if not edad.isdigit() or int(edad) <= 0:
                print("LA EDAD DEBE SER UN NUMERO POSITIVO.")
                continue
            
        
            with open("USUARIOREGISTRADO.txt", "a") as archivo:
                archivo.write(f"Nombre: {nombre}, Email: {correo}, Edad: {edad}, Tipo de ID: {tipoId}, Numero de Id: {numId}\n")
            
            print("¡REGISTRO EXITOSO! LOS DATOS HAN SIDO GUARDADOS")
            
        
            continuar = input("¿DESEA REGISTRAR OTRO USUARIO? (S/N): ").strip().lower()
        except Exception as e:
            print(f"Se produjo un error: {e}")
            break

    print("Finalizando registro...")
