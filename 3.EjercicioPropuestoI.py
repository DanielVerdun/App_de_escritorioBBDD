#REALIZAR UNA APLICACIÓN QUE CONECTE A  BBDD,
#PERMITIENDO AL USUARIO UTILIZAR LA FUNCION C R U D POR MEDIO DE INTERFACE GRÁFICA.

#-------------------------------------------------------------------

from tkinter import *   #---IMPORTAMOS LIBRERIA
import sqlite3
from tkinter import messagebox


#----------FUNCIONES-------------------

def crearConexion():

	conexion=sqlite3.connect("DatosClientes.db")

	miCursor=conexion.cursor()
	
	try:
		miCursor.execute("""CREATE TABLE CLIENTES
		(ID INTEGER PRIMARY KEY AUTOINCREMENT,
		 NOMBRE VARCHAR(15),
		 APELLIDO VARCHAR(15),
	  	 DNI INTEGER,
	  	 EMAIL VARCHAR(30))""")
		messagebox.showinfo("Conexion","La conexion a BBDD fue creada con exito.")
	
	except:
		messagebox.showwarning("¡Atención!","La BBDD ya existe.")

def SalirAplicacion():
	
	valor=messagebox.askquestion("Salir","¿Desea salir de la aplicación?")
	if valor=="yes":
		root.destroy()

def limpiarCampos():
	
	varId.set("")
	varNombre.set("")
	varApellido.set("")
	varDni.set("")
	varEmail.set("")

def insertarCliente():
	
	conexion=sqlite3.connect("DatosClientes.db")

	miCursor=conexion.cursor()

	datos=varNombre.get(),varApellido.get(),varDni.get(), varEmail.get()

	#miCursor.execute("INSERT INTO CLIENTES VALUES(null,'"+varNombre.get()+"','"+varApellido.get()+"','"+varDni.get()+"','"+varEmail.get()+"')")
	miCursor.execute("INSERT INTO CLIENTES VALUES(null,?,?,?,?)",(datos))
	conexion.commit()

	messagebox.showinfo("BBDD","El registro fue insertado con éxito.")
	#conexion.close()

def leerRegistro():

	conexion=sqlite3.connect("DatosClientes.db")

	miCursor=conexion.cursor()

	miCursor.execute("SELECT * FROM CLIENTES WHERE ID=" + varId.get())

	usuario=miCursor.fetchall()

	for dato in usuario:

		varId.set(dato[0])
		varNombre.set(dato[1])
		varApellido.set(dato[2])
		varDni.set(dato[3])
		varEmail.set(dato[4])
		
	conexion.commit()	

def actualizar():

	conexion=sqlite3.connect("DatosClientes.db")

	miCursor=conexion.cursor()
	
	datos=varNombre.get(),varApellido.get(),varDni.get(), varEmail.get()

	#miCursor.execute("UPDATE CLIENTES SET NOMBRE='"+varNombre.get()+"',APELLIDO='"+varApellido.get()+"',DNI='"+varDni.get()+"',EMAIL='"+varEmail.get()+"' WHERE ID="+varId.get())

	miCursor.execute("UPDATE CLIENTES SET NOMBRE=?,APELLIDO=?,DNI=?,EMAIL=? WHERE ID="+varId.get(),(datos))
	
	conexion.commit()

	messagebox.showinfo("BBDD","El registro fue actualizado con éxito.")

"""def eliminar():

	conexion=sqlite3.connect("DatosClientes.db")

	miCursor=conexion.cursor()
    
  	miCursor.execute("DELETE FROM CLIENTES WHERE ID="+varId.get())

   	conexion.commit()

    messagebox.showinfo("BBDD","Registro eliminado con éxito.")"""


#--- VENTANA PRINCIPAL------------------

root=Tk()

root.config(bg="white")
root.title("Ingreso de datos")
root.geometry("800x500")
imagen=PhotoImage(file="Imagen.gif")
Label(root,image=imagen,bd=0).place(x=400,y=90)

miFrame=Frame(root,width=500,height=1)
miFrame.pack(anchor=NW)
miFrame.config(bg="white")

#----BARRA DE MENU----------------------------

barraMenu=Menu(root)
root.config(menu=barraMenu)

bbddmenu=Menu(barraMenu,tearoff=0)
bbddmenu.add_command(label="Conectar",command=lambda:crearConexion())
bbddmenu.add_command(label="Salir",command=lambda:SalirAplicacion())

borrarmenu=Menu(barraMenu,tearoff=0)
borrarmenu.add_command(label="Borrar campos...",command=lambda:limpiarCampos())

crudmenu=Menu(borrarmenu,tearoff=0)
crudmenu.add_command(label="Crear",command=lambda:insertarCliente())
crudmenu.add_command(label="Leer",command=lambda:leerRegistro())
crudmenu.add_command(label="Actualizar",command=lambda:actualizar())
crudmenu.add_command(label="Borrar",command=lambda:())

ayudamenu=Menu(borrarmenu,tearoff=0)
ayudamenu.add_command(label="Licencia")
ayudamenu.add_command(label="A cerca de...")

barraMenu.add_cascade(label="BBDD",menu=bbddmenu)
barraMenu.add_cascade(label="Borrar",menu=borrarmenu)
barraMenu.add_cascade(label="CRUD",menu=crudmenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudamenu)

#----TEXTO DE PANTALLA------------------------

texto1=Label(miFrame,text="ID:")
texto1.config(bg="white")
texto1.grid(row=1,column=0,padx=10,pady=10)

texto2=Label(miFrame,text="Nombre:",bg="white")
texto2.grid(row=2,column=0,padx=10,pady=10)

texto3=Label(miFrame,text="Apellido:",bg="white")
texto3.grid(row=3,column=0,padx=10,pady=10)

texto4=Label(miFrame,text="Dni:",bg="white")
texto4.grid(row=4,column=0,padx=10,pady=10)

texto5=Label(miFrame,text="Comentario:",bg="white")
texto5.grid(row=5,column=0,padx=10,pady=10)

texto6=Label(miFrame,text="Email:",bg="white")
texto6.grid(row=8,column=0,padx=10,pady=10)

#----CUADRO DE TEXTO CORTO---------------------
varId=StringVar()

cuadroTexto1=Entry(miFrame,textvariable=varId)
cuadroTexto1.grid(row=1,column=1,padx=10,pady=10)

varNombre=StringVar()
cuadroTexto2=Entry(miFrame,textvariable=varNombre)
cuadroTexto2.grid(row=2,column=1,padx=10,pady=10)

varApellido=StringVar()
cuadroTexto3=Entry(miFrame,textvariable=varApellido)
cuadroTexto3.grid(row=3,column=1,padx=10,pady=10)

varDni=StringVar()
cuadroTexto4=Entry(miFrame,textvariable=varDni)
cuadroTexto4.grid(row=4,column=1,padx=10,pady=10)

varEmail=StringVar()
cuadroTexto6=Entry(miFrame,textvariable=varEmail)
cuadroTexto6.grid(row=8,column=1,padx=10,pady=10)
#----CUADRO DE TEXTO LARGO----------------------

cuadroTexto5=Text(miFrame)
cuadroTexto5.grid(row=5,column=1,padx=10,pady=10)
cuadroTexto5.config(width=30,height=5)


#----------------BOTONES-----------------------

boton1=Button(miFrame,text="Create",command=lambda:insertarCliente())
boton1.grid(row=6,column=0,padx=10,pady=30)


boton2=Button(miFrame,text="Read",command=lambda:leerRegistro())
boton2.grid(row=6,column=1,padx=10,pady=30)

boton3=Button(miFrame,text="Update",command=lambda:actualizar())
boton3.grid(row=7,column=0,padx=10,pady=10)

boton4=Button(miFrame,text="Delete",command=lambda:())
boton4.grid(row=7,column=1,padx=10,pady=10)






root.mainloop()
