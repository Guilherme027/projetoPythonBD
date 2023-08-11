import mysql.connector 
from mysql.connector import Error

try:
    con = mysql.connector.connect(host='localhost', database='Farmes', user='root',password='P@ssw0rd')

    consulta_sql = "select * from pessoas"
    cursor = con.cursor ()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount)

    print("\nMostrando as pessoas cadastradas")
    for linha in linhas:
        print("id_pessoa:", linha[0])
        print("nome:", linha[1])
        print("sexo:", linha[2])
        print("cargo:", linha[3], "\n")
except Error as e:
    print ("Erro ao acessar ao banco de dados", e)
