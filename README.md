#Actividad 4 - Utilizando sistemas de control de versiones

#Proyecto Registro de Usuarios

## Descripcion
Este proyecto permite registrar usuarios con sus datos personales, como nombre, correo electronico, edad, tipo de identificacion, numero de identificacion
El sistema valida la informacion ingresada y guarda los registros en un archivo.

## Historias de usuario
1. **Historia 1** : Como usuario, se debe registrar el nombre, correo, edad, tipo de identificacion y numero de identificacion.

2. **Historia 2** : Como usuario, se debe validar el correo electronico.

3. **Historia 3** : Se valida en el sistema, la  edad.

4. **Historia 4** : Como administrador se guardan los datos de los usuarios en un archivo.

5. **Historia 5** : Como usuario, se registran varios usarios de manera continua.

#Instalacion.
1. Clonamos el repositorio
git clone https://github.com/ELBA22/MiproyectoIbero.git

2. Navegamos en la carpeta del proyecto
cd repositorio

3. Ejecutamos el script de registro
python registrarusuario.py

#Para hacer un Commit
1. Agregamos el archivo a Git
git add registrarusuario.py

2. Hacemos el Commit con el mensaje que queramos hacer
git commit -m "Primer Commit"

3. Subimos los cambios a GitHub
git push origin main

4. con el comando git status nos muestra el estado actual del repositorio y la rama en la que trabajamos.

GRACIAS...