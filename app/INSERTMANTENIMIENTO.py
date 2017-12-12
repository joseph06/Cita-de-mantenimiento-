
import sqlite3


Servicio = input("Introduzca su Servicio:")
MODELO = input("Introduzca su Modelo:")
AÑO = input("Introduzca su Año:")
PLACA = input("Introduzca su Placa:")
C_SERVICIOS = input("Introduzca su Centro de Servicio:")
DIA_PRE = input("Introduzca su Día de Preferencia:")
HORARIO_PRE = input("Introduzca su Horario de Preferencia:")
KILOMETRAJE = input("Introduzca su Kilometraje:")
TITULO = input("Introduzca su Titulo:")
NOMBRE = input("Introduzca su Nombre:")
APELLIDO = input("Introduzca su Apellido:")
EMAIL = input("Introduzca su Email:")
TELEFONO = input("Introduzca su Telefono:")
CELULAR = input("Introduzca su Celular")
CONTACTO = input("Introduzca su Contacto:")
COMENTARIO = input("Introduzca su Comentario:")


#Establecer la conexión

conexion = sqlite3.connect('proyectop4.db')

#Seleccionar el cursor para iniciar consulta

cursor = conexion.cursor()


#Insertar Daros en la tabla

cursor.execute('''INSERT INTO MANTENIMIENTO(Servicio, MODELO, AÑO, PLACA, C_SERVICIOS, DIA_PRE, HORARIO_PRE, KILOMETRAJE, TITULO, NOMBRE, APELLIDO, EMAIL,TELEFONO, CELULAR,CONTACTO, COMENTARIO)	
		VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')'''%(Servicio,MODELO, AÑO, PLACA,C_SERVICIOS,DIA_PRE,HORARIO_PRE,KILOMETRAJE,TITULO,NOMBRE,APELLIDO,EMAIL,TELEFONO,CELULAR,CONTACTO,COMENTARIO))



#Guardar los cambios en BD
conexion.commit()
#Cerrar la conexion

conexion.close()