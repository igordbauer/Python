import mysql.connector


conexao = mysql.connector.connect(
    host="localhost", user="root", password="ym543t4a", database="crudpython"
)

cursor = conexao.cursor()

# comando = ''
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados
# resultado = cursor.fetchall() # lê do banco de dados


## CREATE
# nome_do_produto = "chocolate"
# valor = 34

# comando = (
#     f'INSERT INTO vendas (nome_produto,valor) VALUES ("{nome_do_produto}",{valor})'
# )
# cursor.execute(comando)
# conexao.commit()

## READ
# comando = f"SELECT * FROM vendas"
# cursor.execute(comando)
# resultado = cursor.fetchall()
# print(resultado)

## UPDATE
# nome_do_produto = "chocolate"
# valor = 6

# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_do_produto}"'
# cursor.execute(comando)
# conexao.commit()

## DELETE

nome_do_produto = "chocolate"

comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_do_produto}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
