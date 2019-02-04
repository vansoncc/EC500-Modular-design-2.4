# EC500-2.4

## Database Module
### Rough code for authentation
```
class authentation:
    def __init__(self):
      self.username = ""
      self.password = ""
    
    def ifmatch(self, username, password):
        do search in authDB
        if match:
            return true
        else:
            return authentation().failure
     
    def failure(self):
        print("Authentation Failed")
        return false
```
#### Rough structure for authDB
```
| username | password | permission |
|   test   |  a123adf |    full    |
```
permission part reserved for future function extension

### for infoDB
```
class infoDB:
    def __init__(self):
        self.personalInfo = {}
        self.bioInfo = {}
        
    def search(self, keyword):
        do search
        return 
    
    def delete(self, keyword):
        do delete
    
    def insert(self, personalInfo, bioInfo):
        self.personalInfo = personalInfo
        self.bioInfo = bioInfo
```
##### DB structure
```
----Personal Info---- | --------------- Bio Info ---------------|
| ID | AGE | gender |.....| Pulse | Heart Rate | Blood Pressure |
```
