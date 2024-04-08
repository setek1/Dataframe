import io
import pandas as pd
import msoffcrypto
import mysql.connector
from pandas import DataFrame
from mysql.connector.abstracts import  MySQLConnectionAbstract


name_db='renta_cargo_db'

def obtener_dataframe_desde_excel_encriptado(ruta_archivo , contraseña) -> DataFrame :
    '''
    
    '''
    decrypted = io.BytesIO()

    with open(ruta_archivo, "rb") as f:
        file = msoffcrypto.OfficeFile(f)
        file.load_key(contraseña)  
        file.decrypt(decrypted)

    df = pd.read_excel(decrypted, sheet_name='ALTOS EJECUTIVOS', header=6)
    print('Realizado')
    return df



def filtrar_informacion(dataframe: DataFrame):
    columnas_a_convertir = ["Sueldo Base Mensual\n$", "Gratificación Mensual\n$", "Asignación Almuerzo \nMensual\n$",
                        "Vales Almuerzo Valor Bruto Mensual\n$", "Valor Casino \n Bruto\nMensual \n$",
                        "Asignación Movilización\nMensual\n$"]
    for columna in columnas_a_convertir:
        dataframe[columna] = pd.to_numeric(dataframe[columna], errors='coerce').fillna(0).astype(int)

    dataframe['Renta_Bruta'] = dataframe[columnas_a_convertir].sum(axis=1)
    
    print('datos procesados con exito')
    return dataframe


def conectar_db(host: str,user: str,password: str):
    try:
        conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            
        )
        print('Conexion exitosa')
        return conexion
    except mysql.connector.Error as error:
        print('Error al conectar a la base de datos: ',error)




def crear_db(conexion:MySQLConnectionAbstract ):
    try:
        cursor = conexion.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {name_db}")
        print(f"Base de datos {name_db} creada con exito")
        cursor.close()
        
    except mysql.connector.Error as error:
        print('Error al crear la base de datos: ',error)
        
    


def crear_tablas(conexion:MySQLConnectionAbstract):
    try:
        cursor=conexion.cursor()
        cursor.execute(f'USE {name_db}')

        create_table_cargos = """
        CREATE TABLE `cargos` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `nombre` varchar(100) DEFAULT NULL,
        `grado` varchar(10) DEFAULT NULL,
        `genero` varchar(2) DEFAULT NULL,
        `nacionalidad` varchar(100) DEFAULT NULL,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
        """
        create_table_rentas = """
        CREATE TABLE `rentas` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `cargo_id` int(11) NOT NULL,
        `renta_bruta` int(11) NOT NULL,
        PRIMARY KEY (`id`),
        CONSTRAINT `fk_cargo_id` FOREIGN KEY (`cargo_id`) REFERENCES `cargos` (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
        """

        cursor.execute(create_table_cargos)
        cursor.execute(create_table_rentas)
        conexion.commit()
        print('TABLAS CREADAS CON EXITO')
        
        


    except mysql.connector.Error as error:
        print('Error al crear las tablas', error)
        return False



def insertar_datos_desde_dataframe(df, conexion:MySQLConnectionAbstract):
    
    try:
        cursor=conexion.cursor()
        cursor.execute(f"USE {name_db}")
        
        

        for index, row in df.iterrows():
            
            nombre_cargo = row["Nombre del Cargo en la Empresa"]
            grado=row["Grado del Cargo según Evaluación Utilizada"]
            genero =row["Género\n(Masculino-Femenino)"]
            nacionalidad=row["Nacionalidad"]
            renta_bruta=row["Renta_Bruta"]
            cursor.execute("INSERT INTO Cargos (nombre,grado,genero,nacionalidad) VALUES (%s,%s,%s,%s)", (nombre_cargo,grado,genero,nacionalidad))
            cargo_id=cursor.lastrowid
            cursor.execute("INSERT INTO Rentas (cargo_id,renta_bruta) VALUES (%s,%s)", (cargo_id, renta_bruta))
            conexion.commit()
        
        
        print('Datos ingresados con exito')

    except mysql.connector.Error as error:
        print('Error al ingresar los datos: ', error)
        print('Existen valores nulos')
    
    finally:
        
        conexion.close()



df=obtener_dataframe_desde_excel_encriptado("./Prueba 1 _Formulario Rentas Altos Ejecutivos C&C.xlsx","123")
df_p=filtrar_informacion(df)
conexion=conectar_db("localhost","root","")
createDB=crear_db(conexion)
crear_tablas(conexion)
insertar_datos_desde_dataframe(df_p,conexion)
