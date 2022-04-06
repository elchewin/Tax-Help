
def run_query(query, parameters = ()):
    conn=sqlite3.connect(db_name)
    c=conn.cursor()
    result = c.execute(query, parameters)
    conn.commit()

    return result


def get_products():
    query = 'SELECT * FROM boleta '
    db_rows = run_query(query)
    print(db_rows)

def add_Usuario():
    if validate_Nombre():
        records = tree.get_children()
        for element in records:
            tree.delete(element)
        conn=sqlite3.connect(db_name)
        c=conn.cursor()
        c.execute('INSERT INTO Usuario VALUES(NULL,:nombre,:peso,NULL,NULL)',
        {
            'nombre':nombre.get(),
            'peso':peso.get()
        })
        conn.commit()
        conn.close()

        message['text'] = 'Usuario {} añadido satisfactoriamente'.format(nombre.get())

        nombre.delete(0, END)
        peso.delete(0, END)
    else:
        message['text'] = 'Nombre y peso requeridos'
    get_Usuarios()