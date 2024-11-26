import mysql.connector

def execute_select_query(query):
    # MySQLに接続
    mydb = mysql.connector.connect(
      host="192.168.0.72",
      port="3306",
      user="administrator",
      password="Akiokapass0",
      database="SC-DB"
    )

    mycursor = mydb.cursor()

    # データを取得するクエリを実行
    mycursor.execute(query)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def execute_insert_query(query):
    # MySQLに接続
    mydb = mysql.connector.connect(
      host="192.168.0.72",
      port="3306",
      user="administrator",
      password="Akiokapass0",
      database="SC-DB"
    )

    mycursor = mydb.cursor()

    # データを挿入するクエリを実行
    mycursor.execute(query)
    mydb.commit()
    print(mycursor.rowcount, "record(s) inserted")
