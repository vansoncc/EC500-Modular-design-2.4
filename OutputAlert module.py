def receive_basic_iuput_data(Singal_Loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension, Hypertension);
	##Recevie data from input module, then analyze it using some judge functions to generate boolean result
	##Boolean Parameters
	##If paramter returns true, means it should be alerted, then add it to the array
	BasicResult = []
	if(Singal_Loss == true) BasicResult.append(Singal_Loss) 
	if(Shock_Alert == true) BasicResult.append(Shock_Alert) 
	if(Oxygen_Supply == true) BasicResult.append(Oxygen_Supply)
	if(Fever == true) return BasicResult.append(Fever) 
	if(Hypotension == true) BasicResult.append(Hypotension)
	if(Hypertension == true) BasicResult.append(Hypertension) 
	return BasicResult


def send_basic_input_data(BasicResult, BasicData);
	## Receive the result and show it on terminal or web page
	analyze(BasicResult)
	return sentData, BasicData;

def receive_AI_iuput_data(Singal_Loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension, Hypertension);
	## Recevie AI data from input module, then analyze it using some judge functions to generate boolean result
	## Paramter is boolean
	## If paramter is true, means it should be alerted, then add it to the array
	AIResult = []
	if(Singal_Loss == true) AIResult.append(Singal_Loss) 
	if(Shock_Alert == true) AIResult.append(Shock_Alert) 
	if(Oxygen_Supply == true) AIResult.append(Oxygen_Supply)
	if(Fever == true) return AIResult.append(Fever) 
	if(Hypotension == true) AIResult.append(Hypotension)
	if(Hypertension == true) AIResult.append(Hypertension) 
	return AIresult;

def send_AI_input_data(AIResult);
	## Receive the result and show it on terminal or web page
	analyze(AIResult)
	return sentData;
