from datetime import datetime

tab_event = []
begin_date = "20/01/2020"
time_event = 30
name = "Session Raclette"

def createEvents(begin_date, time_event, name):
	date = datetime.strptime (begin_date, "%d/%m/%Y")
	res_date = date.timestamp()
	
	event = (res_date, time_event, name)
	print(event)
	return event
	
	
	

