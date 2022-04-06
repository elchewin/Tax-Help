from tkinter import ttk
from tkinter import *

import sqlite3

#---------Librerias---------------------------------
#estructura ventana "Usuarios"

window = Tk()
window.title('Login')
db_name = 'DataBase.db'

conn=sqlite3.connect(db_name)
c=conn.cursor()





#container
frame = LabelFrame(window, text='Agregar boleta')
frame.grid(row=0, column=0, columnspan=3, pady=0)


#NBoleta input
l_NBoleta=Label(frame, text='N° Boleta:')
l_NBoleta.grid(row=1, column=0)
NBoleta = Entry(frame)
NBoleta.grid(row=2, column=0, sticky = W+E)

#mes input
l_mes=Label(frame, text='Mes:')
l_mes.grid(row=3, column=0)
mes = Entry(frame)
mes.grid(row=4, column=0, sticky = W+E)

#Monto input
l_Monto=Label(frame, text='Monto:')
l_Monto.grid(row=5, column=0)
Monto = Entry(frame)
Monto.grid(row=6, column=0, sticky = W+E)

#boton add usuario
sub_b=Button(frame, text='Agregar boleta' ''', command=add_Boleta''' ).grid(row=7, columnspan = 2)

#mensajes
message = Label(text='', fg='red')
message.grid(row=3, column=0, columnspan=2, sticky=W+E)


#tabla
tree = ttk.Treeview(window, height=10, columns=4)
tree.grid(row=4, column=0, columnspan=2)
tree['columns']=("ID","Nombre","Peso")
tree.column("#0", width=0, stretch=NO)
tree.column("ID",width=45, anchor=CENTER)
tree.column("Nombre",width=145, anchor=CENTER)
tree.column("Peso",width=70, anchor=CENTER)

tree.heading('ID', text='ID'  , anchor=CENTER)
tree.heading('Nombre', text='Nombre', anchor=CENTER)
tree.heading('Peso', text='Peso'  , anchor=CENTER)
#llenando filas
#get_Usuarios()




#botones
ttk.Button(text='¿No tienes cuenta?' ''',command=del_Usuario''').grid(row=5, column = 0, sticky = W+E)


ttk.Button(text='Eliminar' ''',command=del_Usuario''').grid(row=5, column = 0, sticky = W+E)
ttk.Button(text='Editar' ''',command=edit_Usuario''').grid(row=5, column = 1, sticky = W+E)

#container2
frame2 = LabelFrame(window, text='opciones')
frame2.grid(row=6, column=0, columnspan=3, pady=10)



conn.commit()
conn.close()
window.mainloop()