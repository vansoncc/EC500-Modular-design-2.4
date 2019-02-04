# EC500-2.4

### System Diagram
<img align = center src = "https://github.com/leonshen95/EC500/blob/master/EC500%20diagram%201.jpg?raw=true">
 
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
|----Personal Info---- | --------------- Bio Info ---------------|
| ID | AGE | gender |.....| Pulse | Heart Rate | Blood Pressure |
```


## Display Module


### Input:
* Emergency: when the data is analyzed to be vital 
* Signal loss alert: when sensor is lost attached
* Shock alert: when patient is in shock
* Oxygen supplement alert: patient does not enough oxygen, needs to increase amount of oxygen

Condition: Normal
* Fever sign: light is still on
* Hypotension and hypertension sign: light is still on

Condition: AI - based module -- prediction alert

Normal parameters: Pulse, Blood pressure, Blood Oxygen

### Output:
* Pulse: pulse on configurable time intervals
* Blood pressure: blood pressure on configurable time intervals
* Blood Oxygen: blood Oxygen levels on configurable time intervals
* Whether to get alerts
* Get future prediction based on AI module

### Class and Interface:
class Alerts {
* Objects: Signal loss alert, Shock alert, Oxygen supplement alert, Prediction alert
* method: receiveAlerts(Objects), judgeAlerts(Objects), sendAlerts()

}

class normalParameter {
* Objects: Pulse, Blood pressure, Blood Oxygen
* method: receiveParameter(Objects), handleParameter(Objects), sendParameter(),

}
