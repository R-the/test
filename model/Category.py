from model.DatabasePool import DatabasePool

class Category:

    @classmethod  
    def insertCategory(cls,name,description): 

        try: 
            #get connection
            dbConn=DatabasePool.getConnection()
            #Define cursor to run query(after connection created)
            cursor = dbConn.cursor(dictionary=True)

            #Specify Sql Statement ***  
            sql="Insert into category(name,description) values(%s,%s)" 

            #Run Query(Using cursor)
            cursor.execute(sql,(name,description)) 
           
            #for INSERT,UPDATE,DELETE to EFFECT THE DATABASE
            dbConn.commit() 
            
            #ROWCOUNT
            rows=cursor.rowcount 
            return rows
        finally: #Release connection back to connection pool
            dbConn.close()


    
    #Retrieve all category)
    @classmethod
    def getAllCategory(cls):

        try: 
            #get connection
            dbConn=DatabasePool.getConnection()
            #Define cursor to run query(after connection created)
            cursor = dbConn.cursor(dictionary=True)

            #Specify Sql Statement ***
            sql="select * from category" 

            #Run Query(Using cursor)
            cursor.execute(sql,()) 
           
            #fetchall()method to fetch everything into curcor
            users = cursor.fetchall()
            return users 

        finally: #Release connection back to connection pool
            dbConn.close()
