class intput
    def __init__(self, user_id, age, gender, heartrate, Systolic_BP, DIastolic_BP, blood_oxygen, temperature):
        # self.user_id = user_id
        # self.age = age
        # self.gender = gender
        # self.heartbeat = heartbeat
        # self.blood_pressure = blood_pressure
        # self.blood_oxygen = blood_oxygen
        # self.temperature = temperature
        #Systolic_BP
        #Diastolic_BP
        self.dic = {"user_id": user_id， "gender": gender, "heartrate": heartrate, "Diastolic_BP": Diastolic_BP, "Systolic_BP":Systolic_BP, "blood_oxygen": blood_oxygen, "temperature": temperature, "time": time}

    def filter(data, noise, data_type):
        wrong = -100
        if data > noise:
            data = wrong
        return data

    def return data(dic):
        for key in dic.keys():
            if (key != "user_id" and key != "age" and key != "gender"):
                dic[key] = filter(dic[key], noise, key)

    def return_request(wire):
        alert = 1
        user_db = 2
        data_db = 3
        if (wire == alert):
            return alert_data
        if (wire == user_db):
            return user_info
        if (wire == data_db):
            return user_data & user_info





#the user have the access to the patient cases in database, which contains the basic infomation and the fitness data
#the user can only have the access to his own data
#For the input function, are devided into different user groups which has different permission to access the database.
#Once connected, It will also connect the hardware device to the internet, which enable it to use store the data into the user's directory.
