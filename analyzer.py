Signal_Loss = False
Shock_Alert = False
Oxygen_Supply = False
Fever = False
Hypotension = False
Hypertension = False

def analyzer(Systolic_BP, Diastolic_BP, Heart_Rate, Heart_O2_Level, Body_temp):
    global Signal_Loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension, Hypertension

    if (Systolic_BP < 90 and Diastolic_BP < 60):
        Hypotension = True
    else:
        Hypotension = False

    if (Systolic_BP > 140 or Diastolic_BP > 90):
        Hypertension = True
    else:
        Hypertension = False

    if (Heart_Rate < 60 and Body_temp < 36):
        Signal_Loss = True
    elif (Heart_Rate < 60 and Body_temp >= 36):
        Shock_Alert = True
    else:
        Signal_Loss = False
        Shock_Alert = False
    
    if (Body_temp > 37.5):
        Fever = True
    else:
        Fever = False

    if (Heart_O2_Level < 70):
        Oxygen_Supply = True
    else:
        Oxygen_Supply = False
