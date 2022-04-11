from msilib.schema import ComboBox
from multiprocessing.sharedctypes import Value
from tkinter import ttk
from tkinter import *
import sqlite3


db_name = 'DataBase.db'
conn = sqlite3.connect(db_name)
c = conn.cursor()

# ---------Librerias---------------------------------
# estructura ventana "Usuarios"
window = Tk()
window.title('Tax Help')


def edit_boleta():

    try:
        tree.item(tree.selection())['values'][0]
    except IndexError as e:
        return

    global ID_u
    ID_u = tree.item(tree.selection())['values'][0]
    global old_mes
    old_mes = tree.item(tree.selection())['values'][1]
    old_Monto = tree.item(tree.selection())['values'][2]

    global edit_wind
    edit_wind = Toplevel()
    edit_wind.title = 'Editar Boleta'

    # Old MES
    Label(edit_wind, text='Mes anterior: ').grid(row=0, column=1)
    Entry(edit_wind, textvariable=StringVar(edit_wind, value=old_mes),
          state='readonly').grid(row=0, column=2)

    # New MES
    Label(edit_wind, text='Nuevo Mes').grid(row=1, column=1)
    global new_mes
    new_mes = ttk.Combobox(edit_wind, values=[
        'enero',
        'febrero',
        'marzo',
        'abril',
        'mayo',
        'junio',
        'julio',
        'agosto',
        'septiembre',
        'octubre',
        'noviembre',
        'diciembre'
    ])
    new_mes.grid(row=1, column=2)

    # Old MONTO
    Label(edit_wind, text='Monto anterior: ').grid(row=2, column=1)
    Entry(edit_wind, textvariable=StringVar(edit_wind, value=old_Monto),
          state='readonly').grid(row=2, column=2)
    # New MONTO
    Label(edit_wind, text='Nuevo Monto').grid(row=3, column=1)
    global new_Monto
    new_Monto = Entry(edit_wind)
    new_Monto.grid(row=3, column=2)

    Button(edit_wind, text='Editar', command=edit_records).grid(
        row=4, column=2, sticky=W)


def edit_records():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute('UPDATE Boletas SET mes=:mes, Monto=:Monto WHERE N_boleta=:ID',
              {
                  'mes': new_mes.get(),
                  'Monto': new_Monto.get(),
                  'ID': ID_u
              })

    conn.commit()
    conn.close()

    edit_wind.destroy()
    get_boleta()


def add_boleta():

    if validate_boleta():
        records = tree.get_children()
        for element in records:
            tree.delete(element)

        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        c.execute('INSERT INTO Boletas VALUES(NULL,:mes,:Monto)',
                  {
                      'mes': mes.get(),
                      'Monto': Monto.get()
                  })
        conn.commit()
        conn.close()

        mes.delete(0, END)
        Monto.delete(0, END)
    get_boleta()


def del_boleta():

    try:
        tree.item(tree.selection())['values'][0]
    except IndexError as e:
        return

    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    ID_u = tree.item(tree.selection())['values'][0]

    c.execute('DELETE FROM Boletas WHERE N_boletas='+str(ID_u))

    conn.commit()
    conn.close()

    get_boleta()


def get_tramo():
    # limpiando la tabla
    records = tree1.get_children()
    for element in records:
        tree1.delete(element)

    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute('SELECT * FROM Tramos ORDER BY ID DESC')
    db_filas = c.fetchall()

    # recorriendo y rellenando los datos
    for fila in db_filas:
        tree1.insert('', 0, text='', values=(
            fila[1], fila[2], fila[3], fila[4]))
    conn.commit()
    conn.close()


def get_boleta():
    # limpiando la tabla
    records = tree.get_children()
    for element in records:
        tree.delete(element)

    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute('SELECT * FROM Boletas ORDER BY N_boletas DESC')
    db_filas = c.fetchall()

    montoTotal = 0
    # recorriendo y rellenando los datos
    for fila in db_filas:
        montoTotal = montoTotal+fila[2]
        tree.insert('', 0, text='', values=(fila[0], fila[1], fila[2]))

    if(montoTotal < 9185220):
        montoTotal = montoTotal*0.7

    conn.commit()
    conn.close()
    return montoTotal


def validate_boleta():
    return len(mes.get()) != 0 and len(Monto.get()) != 0


# container
frame = LabelFrame(window, text='Agregar boleta')
frame.grid(row=0, column=0, columnspan=3, pady=0)


# mes input
l_mes = Label(frame, text='Mes:')
l_mes.grid(row=1, column=0, sticky=W)
mes = ttk.Combobox(frame, values=[
    'enero',
    'febrero',
    'marzo',
    'abril',
    'mayo',
    'junio',
    'julio',
    'agosto',
    'septiembre',
    'octubre',
    'noviembre',
    'diciembre'
])
mes.grid(row=1, column=1)

# Monto input
l_Monto = Label(frame, text='Monto:')
l_Monto.grid(row=2, column=0)
Monto = Entry(frame)
Monto.grid(row=2, column=1)


# boton add usuario
sub_b = Button(frame, text='Agregar boleta', command=add_boleta)
sub_b .grid(row=3, columnspan=2, sticky=W+E)


wrapper1 = LabelFrame(window, text="")
wrapper1.grid(row=1, column=0, columnspan=3, pady=0)
# tabla

tree = ttk.Treeview(wrapper1, height=10, columns=4)
tree.pack(side=LEFT)
tree['columns'] = ("N° Boleta", "Mes", "Monto")
tree.column("#0", width=0, stretch=NO)
tree.column("N° Boleta", width=60, anchor=CENTER)
tree.column("Mes", width=70, anchor=CENTER)
tree.column("Monto", width=100, anchor=CENTER)

tree.heading('N° Boleta', text='N° Boleta', anchor=CENTER)
tree.heading('Mes', text='Mes', anchor=CENTER)
tree.heading('Monto', text='Monto', anchor=CENTER)
# llenando filas
get_boleta()

tree1 = ttk.Treeview(wrapper1, height=10, columns=4)
tree1.pack(side=RIGHT)
tree1['columns'] = ("Desde", "Hasta", "Factor", "Cantidad a rebajar")
tree1.column("#0", width=0, stretch=NO)
tree1.column("Desde", width=75, anchor=W)
tree1.column("Hasta", width=100, anchor=W)
tree1.column("Factor", width=50, anchor=CENTER)
tree1.column("Cantidad a rebajar", width=105, anchor=W)

tree1.heading('Desde', text='Desde', anchor=CENTER)
tree1.heading('Hasta', text='Hasta', anchor=CENTER)
tree1.heading('Factor', text='Factor', anchor=CENTER)
tree1.heading('Cantidad a rebajar', text='Cantidad a rebajar', anchor=CENTER)
# llenando filas
get_tramo()


# botones
ttk.Button(text='Eliminar', command=del_boleta).grid(
    row=5, column=0, sticky=W+E)
ttk.Button(text='Editar', command=edit_boleta).grid(
    row=5, column=1, sticky=W+E)


montoTotal = get_boleta()


def taxHelp(montoTotal):

    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('SELECT factor,cantidad_rebajar FROM Tramos WHERE desde<' +
              str(montoTotal)+' AND hasta>'+str(montoTotal))
    datos1 = c.fetchall()
    conn.commit()
    conn.close()
    try:
        datos = datos1[0]
        factor = datos[0]
        cantRebajar = datos[1]
        impuRetenido = montoTotal*0.1225
        return (montoTotal*factor)-cantRebajar-impuRetenido
    except IndexError as e:
        return 0


# container2
frame2 = LabelFrame(window, text='Datos de interes')
frame2.grid(row=6, column=0, columnspan=3, pady=10)
# botones
Label(frame2, text='-Monto total (*): '+str(montoTotal)
      ).grid(row=5, column=0, sticky=W)
Label(frame2, text='-Impuesto retenido: ' +
      str(montoTotal*0.1225)).grid(row=6, column=0, sticky=W)

res = taxHelp(montoTotal)

if(res < 0):
    Label(frame2, text='-Te devuelven: '+str(res*-1)
          ).grid(row=7, column=0, sticky=W)
else:
    Label(frame2, text='-Pagas: '+str(res)).grid(row=7, column=0, sticky=W)


Label(window, text='(*) teniendo en cuenta el 30'+'%' +
      ' de gastos presuntos').grid(row=8, column=0, sticky=W)


window.mainloop()
