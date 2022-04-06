from tkinter import ttk
from tkinter import *

import API

#---------Librerias---------------------------------
#estructura ventana "Usuarios"
window = Tk()
window.title('Tax Help')


#container
frame = LabelFrame(window, text='Agregar boleta')
frame.grid(row=0, column=0, columnspan=3, pady=0)


#mes input
l_mes=Label(frame,text='Mes:')
l_mes.grid(row=1, column=0)
mes = Entry(frame)
mes.grid(row=1, column=1)

#Monto input
l_Monto=Label(frame, text='Monto:')
l_Monto.grid(row=2, column=0)
Monto = Entry(frame)
Monto.grid(row=2, column=1)

#boton add usuario
sub_b=Button(frame, text='Agregar boleta' , command=API.add_boleta ).grid(row=3, columnspan = 2, sticky = W+E)


#tabla
tree = ttk.Treeview(window, height=10, columns=4)
tree.grid(row=4, column=0, columnspan=2)
tree['columns']=("ID","Mes","Monto")
tree.column("#0", width=0, stretch=NO)
tree.column("ID",width=45, anchor=CENTER)
tree.column("Mes",width=145, anchor=CENTER)
tree.column("Monto",width=70, anchor=CENTER)

tree.heading('ID', text='ID'  , anchor=CENTER)
tree.heading('Mes', text='Mes', anchor=CENTER)
tree.heading('Monto', text='Monto'  , anchor=CENTER)
#llenando filas
#get_Usuarios()

#botones
ttk.Button(text='Eliminar',command="del_Usuario").grid(row=5, column = 0, sticky = W+E)
ttk.Button(text='Editar' ,command="edit_Usuario").grid(row=5, column = 1, sticky = W+E)

#container2
frame2 = LabelFrame(window, text='opciones')
frame2.grid(row=6, column=0, columnspan=3, pady=10)

#botones
ttk.Button(frame2, text='Rutinas', command="win_Rutina").grid(row=5, column = 0, sticky = W+E)
ttk.Button(frame2, text='Comidas del día', command="win_Comidas").grid(row=5, column = 1, sticky = W+E)
ttk.Button(frame2, text='Progreso de Peso', command="win_P_peso").grid(row=6, column = 0, sticky = W+E)
ttk.Button(frame2, text='Progreso de Medidas', command="win_P_medidas").grid(row=6, column = 1, sticky = W+E)

window.mainloop()