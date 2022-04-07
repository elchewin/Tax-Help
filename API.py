import sqlite3
from tkinter import Entry
from tkinter.ttk import Treeview

db_name = 'DataBase.db'
conn = sqlite3.connect(db_name)
c = conn.cursor()


def run_query(query, parameters=()):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    result = c.execute(query, parameters)
    conn.commit()

    return result


def get_boleta(tree: Treeview):
    # limpiando la tabla
    records = tree.get_children
    for element in records:
        tree.delete(element)

    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute('SELECT * FROM Boleta ORDER BY N_boleta DESC')
    db_filas = c.fetchall()

    # recorriendo y rellenando los datos
    for fila in db_filas:
        tree.insert('', 0, text='', values=(fila[0], fila[1], fila[2]))
    conn.commit()
    conn.close()


def add_boleta(mes, Monto, tree: Treeview):

    records = tree.get_children()
    for element in records:
        tree.delete(element)

    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    c.execute('INSERT INTO Boletas VALUES(NULL,:mes,:Monto)',
              {
                  'mes': mes,
                  'Monto': Monto
              })
    conn.commit()
    conn.close()

    get_boleta(tree)


'''
    def get_products():
    records = tree.get_children()
    for element in records :
        tree.delete(element)

    query = 'SELECT * FROM boleta '
    db_rows = run_query(query)
    #rellenando datos 
    for row in db_rows:
        
        tree.insert('', 0, text = row [1], values=[2])
'''
