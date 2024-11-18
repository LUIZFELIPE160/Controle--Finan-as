import sqlite3 as lite 

# criando conexão
con = lite.connect('dados.db')

# inserir categoria 
def inserir_categoria(i):
    with con:   #  este comando WITH  faz com que este bloco seja fechado quando finalizado.
        cur =  con.cursor()
        query = " INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query, i)

# inserir receitas
def inserir_receitas(i):
    with con:  
        cur =  con.cursor()
        query = " INSERT INTO receitas (categoria, adicionado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)

# inserir despesas
def inserir_despesas(i):
    with con:   
        cur =  con.cursor()
        query = " INSERT INTO despesas (categoria, adicionado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)

# funcoes para deletar---------------------------------------------
def del_receitas(i):
    with con :
        cur = con.cursor()
        query = "DELETE FROM Receitas where id= ?"
        cur.execute(query, i)

def del_despesas(i):
    with con :
        cur = con.cursor()
        query = "DELETE FROM Despesas where id= ?"
        cur.execute(query, i)

# ver dados ---------------------------------------

# categoria
def ver_categoria ():
    lista_itens=[]

    with con :
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        linha = cur.fetchall()
        
        for l in linha:
            lista_itens.append(l)

        return lista_itens
    
print(ver_categoria())

# categoria
def ver_categoria ():
    lista_itens=[]

    with con :
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        linha = cur.fetchall()
        
        for l in linha:
            lista_itens.append(l)

        return lista_itens
    
# Despesas
def ver_despesas ():
    lista_itens=[]

    with con :
        cur = con.cursor()
        cur.execute("SELECT * FROM Despesas")
        linha = cur.fetchall()
        
        for l in linha:
            lista_itens.append(l)

        return lista_itens
    
## ADICIONAR UPDATE FUTURAMENTE