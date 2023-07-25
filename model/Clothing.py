from model.DatabasePool import DatabasePool

class Clothing:
    @classmethod
    def getClothingByStringName(cls, categoryID):
        
        try:
            #connection
            dbConn=DatabasePool.getConnection()
            #use cursor
            cursor=dbConn.cursor(dictionary=True)
           
            sql="select * from clothing where categoryID=%s order by price asc"

            # sql ="select * from clothing where name like %s"
            

            #execute
            cursor.execute(sql,(categoryID,))
            #fetch
            matches=cursor.fetchall()
            return matches
        
        finally:#release
            dbConn.close()

    @classmethod
    def getAllClothings(cls):
        try:
            #connect to database
            dbConn = DatabasePool.getConnection()
            #use cursor to get everything from dict
            cursor = dbConn.cursor(dictionary=True)
            #sql statement 
            sql="select * from clothing"
            #execute
            cursor.execute(sql,()) 
            #fetch everthing
            category=cursor.fetchall()
            return category

        finally:
            #close database
            dbConn.close()            