        =*Repositorio grupo 4*=

Integrantes:
- Badir Villegas - 202273020-K
- Benjamin Reyes - 202273053-6
- Fernanda Ojeda - 202273025-0
- Sebastian Reyes -202273105-2

## Wiki

Puede acceder a la wiki del repositorio mediante el siguiente [enlace](https://gitlab.com/grupo4-2024-proyinf/GRUPO4-2024-PROYINF/-/wikis/Wiki)

## Enlace video hito 3
Puede acceder al video del prototipo en el siguiente [enlace](https://youtu.be/PczyER8rk8M)

## Enlace video hito 5
Puede acceder al video del resultado final en el siguiente [enlace](https://youtu.be/jyo13oVk6SY)


## Pasos para levantar el proyecto:

1. **Clonación del repositorio**: Asegúrese de clonar el repositorio en su dispositivo utilizando uno de los siguientes enlaces:
   - HTTPS: `https://gitlab.com/grupo4-2024-proyinf/GRUPO4-2024-PROYINF.git`
   - SSH: `git@gitlab.com:grupo4-2024-proyinf/GRUPO4-2024-PROYINF.git`

2. **Verificación de Docker**: Asegúrese de tener Docker instalado en su dispositivo. Abra la carpeta del proyecto en Visual Studio Code y ejecute el siguiente comando en la terminal:
   ```bash
   docker-compose up --build
   ```
   *Nota: Si ya tiene la imagen construida, puede usar simplemente `docker-compose up`.*

3. **Conectar el proyecto al contenedor**:
   - Si está utilizando Visual Studio Code en Windows, seleccione la opción **'Open Remote Window'**. Esto abrirá un menú con varias opciones. Seleccione **'Attach to Running Container...'**.
   - A continuación, elija la opción **'/grupo04-2024-proyinf-web-1'**. Esto conectará Visual Studio Code al contenedor utilizando una distribución de Linux.

4. **Ejecutar comandos en la terminal**:
   - Navegue al directorio del proyecto:
     ```bash
     cd RendicionDeGastos
     ```
   - Inicie el servidor de desarrollo de Django:
     ```bash
     python manage.py runserver 8080
     ```


    