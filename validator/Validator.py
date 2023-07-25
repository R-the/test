import functools
from flask import Flask,jsonify,request


from model.User import User



def admin_login(func):
    @functools.wraps(func)
    def checkAdmin(**kwargs):
        
        try:
        #request.json
            # email=kwargs["email"]
            # password=kwargs["password"]
            
            email=request.json['email']
            password=request.json['password']
        
        
            users=User.loginUser(email,password) #use loginUser to validate
        
        
            jsonResult={"Users":users}
            return jsonify(jsonResult),200 #OK
        
        except Exception as err:
            print(err)                    #+str(err)
            return jsonify({"Message":"You are not authorised!"}),401 #Unauthorised

               
        # else:
        #     value=func(*args,**kwargs)
        #     return value
    
    return checkAdmin