import sqlite3

conexion = sqlite3.connect('proyectop4.db')
cursor = conexion.cursor()

#Crear Tabla
cursor.execute('''CREATE TABLE MANTENIMIENTO
		(Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
		Servicio TEXT NOT NULL,
		MODELO TEXT NOT NULL,
		AÑO INT NOT NULL,
		PLACA TEXT NOT NULL,
		C_SERVICIOS TEXT NOT NULL,
		DIA_PRE DATE NOT NULL,
		HORARIO_PRE TIME NOT NULL,
		KILOMETRAJE TEXT NOT NULL,
		TITULO TEXT NOT NULL,
		NOMBRE TEXT NOT NULL,
		APELLIDO TEXT NOT NULL,
		EMAIL TEXT NOT NULL,
		TELEFONO TEXT NOT NULL,
		CELULAR TEXT NOT NULL,
		CONTACTO TEXT NOT NULL,
		COMENTARIO TEXT NOT NULL)''')


#Terminamos la consulta
conexion.close()