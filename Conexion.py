import mariadb
class conexion:

    def __init__(self):
            try:
                self.conn=mariadb.connect(
                    host="localhost",
                    user="root",
                    #password="123456789",
                    password="admin",
                    database="Pensionado",
                    autocommit=True
                )
                print("Conexion exitosa")
            except mariadb.Error as e:
                print("Error al conectarse a la bd",e)

    def consultaBD(self,query):
        try:
            cur = self.conn.cursor()
            id2=cur.execute(query)
            print("PRIMERO   "+str(id2))
            
            return cur
        except mariadb.Error as e:
            print(e)
