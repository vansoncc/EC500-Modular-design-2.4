def Query_Data_From_Database(time):
    ## connect database, query previous one day data from Database

    return PreviousData

def Get_Real_Time_Data():
    ## Get the real-time data and inout to AI module
    return RealTimeData

def AI_Module(PreviousData, RealTimeData):
    ## AI module do the prediection, The AI module uses previous data and compared with 
    ## real-time data to predict the future trend 
    return AI_Prediction_result

def Feedback(AI_Prediction_result):
    ## feedback the AI prediction restult to the interface 
    ## It will turn on the Alert when the statues get worse.
    return feedback