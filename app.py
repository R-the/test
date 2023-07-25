from flask import Flask,jsonify,request
from model.User import User
from model.Category import Category
from model.Clothing import Clothing
from validator.Validator import *

app = Flask(__name__)

######################
#Get All Users 
######################

@app.route('/users', methods=["GET"]) 
@admin_login
def getUsers():
    
    try:
       
            users=User.getAllUsers()
            jsonUsers={"Users":users}
            return jsonify(jsonUsers),200 
    except Exception as err:
        print(err)
        return jsonify({"Message":"Error Ocurred!"}),500



###########################
#Verify admin’s credentials 
#using email and password 
###########################

@app.route('/users/login', methods=["POST"]) 
def loginUser():
    try:
        #request.json
      
        email=request.json['email']
        password=request.json['password']
       

        #Update rows
        users=User.loginUser(email,password)
       
       
        # output=str(rows)+ " row(s) updated" 
        jsonResult={"Users":users}
        return jsonify(jsonResult),200 #UPDATED!
    except Exception as err:
        print(err)                    #+str(err)
        return jsonify({"Message":"Error Occurred!"}),500
    


#################
#Add new clothing 
#################

###################################
@app.route('/users/clothing', methods=["POST"])
@admin_login
def insertClothing():
    try:
        #request.json
        # clothingID=request.json['clothingID']
        name=request.json['name']
        description=request.json['description']
        image_url=request.json['image_url']
        categoryID=request.json['categoryID']
        price=request.json['price']
        # DateInserted=request.json['DateInserted']

      
        rows=User.insertClothing(name,categoryID,description,image_url,price)
       
        #json object ->UPDATE RESULT MESSAGE
        output=str(rows)+ " row(s) inserted" 
        jsonResult={"Message":output}
        return jsonify(jsonResult),201 #Created
    except Exception as err:
        print(err)
        return jsonify({"Message":"Error Occurred!"}),500

######################################

#################
#Add new category
#################  

@app.route('/users/category', methods=["POST"]) 
@admin_login
def insertCategory():
    try:
        #request.json
        name=request.json['name']
        description=request.json['description']
       

        rows=Category.insertCategory(name,description)
       
        #json object ->UPDATE RESULT MESSAGE
        output=str(rows)+ " row(s) inserted" 
        jsonResult={"Message":output}
        return jsonify(jsonResult),201 #Created
    except Exception as err:
        print(err)
        return jsonify({"Message":"Error Occurred!"}),500


######################
#Retrieve all category
######################
#Get All Category
@app.route('/users/getallcategory', methods=["GET"])
def getAllCat():
    try:
        category=Category.getAllCategory()
        jsonUsers={"Category":category}
        return jsonify(jsonUsers),200 
    except Exception as err:
        print(err)
        return jsonify({"Message":"Error Ocurred!"}),500

######################
#Retrieve all clothing
###################### 
#Get All Clothings

@app.route('/users/getallclothings' , methods=["GET"])
def getAllCategory():
    try:
        jsonAllClothings=Clothing.getAllClothings()
        jsonAllCloths={"Category":jsonAllClothings}
        # print(jsonCat)
        return jsonify(jsonAllCloths),200
    
    except Exception as err:
        print(err)
        return jsonify({"Message":"Error Ocurred!"}),500
    

#############################
#Retrieve all clothings 
#based on typeID & asc price
#############################
    #Match Category ID of clothing
@app.route('/users/clothings/<int:categoryID>' , methods=["GET"])
def getClothingByCat(categoryID):
    try:
        clothings=Clothing.getClothingByStringName(categoryID)
        #json
        jsonClothings={"Clothings":clothings}
        return jsonify(jsonClothings),200 #OK
    except Exception as err:
        print(err)
        return jsonify({"Message":"Error Ocurred!"}),500 #Internal Server Error
    


if __name__=="__main__":
    app.run(debug=True)    