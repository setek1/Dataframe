# 1. Gestor de base de datos
Para trabajar con base de datos MySQL en este proyecto se utilizó el software xampp, este se debe ejecutar por lo que se debe abrir el panel de control y damos 'start' a las opciones de apache y Mysql, en el caso contrario a continuación se deja el link de descarga:
* [XAMPP](https://www.apachefriends.org/es/index.html)




# 2. Python y pip
Una vez clonado el repositorio lo primero que se debe realizar es verificar si se tiene instalado Python y pip, para esto se deberá ocupar los siguientes comandos en consola:
```bash
python --version
```
```bash
pip --version
```

En el caso de no tenerlas instaladas dirigirse a los siguientes links:
* [python](https://www.python.org/)
* [pip](https://pypi.org/project/pip/)



# 3. Entorno virtual
Se deberá instalar virtualenv usando pip, posteriormente a esto se tiene que crear un entorno virtual dentro del proyecto con el nombre que uno estime conveniente.
```bash
pip install virtualenv
```
Se recomienda crear la carpeta en la raíz del proyecto.
```bash
virtualenv nombre_archivo
```
Una vez creado el entorno virtual se deberá acceder a este, es importante recalcar que se debe estar dentro de la ruta de donde se encuentra este archivo, para esto se ocupara este comando:
```bash
.\nombre_archivo\Scripts\activate
```
Para comprobar que estamos dentro del entorno virtual en la parte izquierda de nuestra ruta podremos ver entre paréntesis el nombre que se escogió para el entorno virtual, a continuación se puede ver un ejemplo.
```bash
(venv) PS C:\ejemplo\ejemplo\ejemplo>
```

# 4 Archivo
El archivo a trabajar se debe copiar en la raíz del proyecto para que así el sistema pueda leerlo, en el caso contrario cambiar el primero parámetro de la función obtener_dataframe_desde_excel_encriptado a la ruta correspondiente.

# 5. Instalación de requerimientos
Dentro del proyecto existe un archivo llamado requirements.txt este debe ser ejecutado dentro del entorno virtual con el siguiente comando:
```bash
pip install -r requirements.txt
```
Este comando instalara todas las dependencias necesarias para poder ejecutar el proyecto.
# 6. Ejecución del proyecto
Una vez configurado el entorno virtual, instalado las dependencias y corriendo xampp, es posible ejecutar este proyecto sin problemas el cual se puede hacer apretando el botón de ejecución de Python o con el siguiente comando:
```bash
python .\p_tecnica.py
```
# 7. Nuevo archivo Excel
Se creará un nuevo archivo excel en donde se podrá visualizar los cambios que se hicieron en el.

# 8. ❗Importante❗
Este proyecto genera de forma automática la base de datos y sus propias tablas al ejecutarlo, por lo que no es necesario el uso de script SQL antes de ejecutarlo, la base de datos usada es MySQL con el software xampp, lo más crítico es introducir de forma correcta las credenciales para que el proyecto se puede conectar sin errores a la BD, las credenciales que se ocupan para este proyecto son:

```json
{
  "host": "localhost",
  "user": "root",
  "password": ""
}
```




