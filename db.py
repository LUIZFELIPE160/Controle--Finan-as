import sqlite3 as lite 

con = lite.connect('dados.db')

# criando tabela categoria
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")


# criando tebela receitas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Receitas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL)")



# criando tebela despesas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Despesas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirada_em DATE, valor DECIMAL)")