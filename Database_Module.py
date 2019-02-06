authenDB = {'admin':"123456"}
infoDB = {}
class DataBaseModule:
    
    def __init__(self,infoDB,authDB):
        self.username = ""
        self.password = ""
        self.infoDB = infoDB
        self.authDB = authDB
        self.auth = False
    

    def authen(self, authenDB, username, password):
        self.username = username
        self.password = password
        if authenDB[self.username] == self.password:
            print("Authentication Succeed!")
            self.auth = True
        else:
            print("Try username and password again")


    def delete(self, ID):
        if self.auth:
            infoDB.popitem(ID)
        else:
            print ("Authentation Failed")
    
    def insert(self,ID,info):
        if self.auth:
            infoDB[ID] = info
        else:
            print("Authentation Failed")
            
    
    def search(self,ID):
        if self.auth:
            return self.infoDB[ID]
        else:
            print("Authentation Failed")
    



