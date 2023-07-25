from mysql.connector import pooling

class DatabasePool: #name of class
    #class variables
    connection_pool = pooling.MySQLConnectionPool( #database pool (port:3306(default))
                               pool_name="ws_pool",
                               pool_size=5, #no. of connections to maintain
                               host='localhost', 
                               database='sp_fashion',#Name of schema
                               user='root', #sql workbench username
                               password='root') #sql workbench password

    #connect to database
    @classmethod #the Class=(instance) #only 1 database pool
    def getConnection(cls): #cls=Class (parameter)
        dbConn = cls.connection_pool.get_connection()
        return dbConn
