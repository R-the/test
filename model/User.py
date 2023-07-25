from model.DatabasePool import DatabasePool


class User:
    
    @classmethod
    def getAllUsers(cls): #Class

        try: 
            #get connection
            dbConn=DatabasePool.getConnection()
            #Define cursor to run query(after connection created)
            cursor = dbConn.cursor(dictionary=True)

            #Specify Sql Statement ***
            sql="select * from user" 

            #Run Query(Using cursor)
            cursor.execute(sql,()) 
           
            #fetchall()method to fetch everything into curcor
            users = cursor.fetchall()
            return users 

        finally: #Release connection back to connection pool
            dbConn.close()





    # EMAIL & PASSWORD RECORD 
    @classmethod   
    def loginUser(cls,email,password): 

        try: 
            #get connection
            dbConn=DatabasePool.getConnection()
            #Define cursor to run query(after connection created)
            cursor = dbConn.cursor(dictionary=True)

            #Specify Sql Statement ***   
            sql="select * from user where email = %s and password =%s"

            #Run Query(Using cursor) 
                                        
            cursor.execute(sql,(email,password))
            
            user=cursor.fetchone()
            
            if email=="mary_jane@gmail.com" and password=="mary123": #no matching record
                user=User.getAllUsers()
                
                return user
            else:
                return "" #"You are not authorised!"

        finally: #Release connection back to connection pool
            dbConn.close()


    #Add New Clothing [POST]
    @classmethod   
    def insertClothing(cls,name,categoryID,description,image_url,price): 

        try: 
            #get connection
            dbConn=DatabasePool.getConnection()
            #Define cursor to run query(after connection created)
            cursor = dbConn.cursor(dictionary=True)

            #Specify Sql Statement ***   #user.userid
            sql="Insert into clothing(name,categoryID,description,image_url,price) values(%s,%s,%s,%s,%s)"

            cursor.execute(sql,(name,categoryID,description,image_url,price)) 
           
            dbConn.commit() 
            
            #ROWCOUNT
            rows=cursor.rowcount
            return rows
        finally: #Release connection back to connection pool
            dbConn.close()
