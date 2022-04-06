
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
