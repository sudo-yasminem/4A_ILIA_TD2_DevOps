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
	

def Get_events():
	return tab_event
	print(tab_event)


def add_events(event, tab_event):
	tab_event.append(event)
	return tab_event

def first_event(tab_event):
	print(tab_event[0])
	return tab_event[0]


#A finir
def sort_events(tab_event):
	tab_event_sorted = []
	for i in tab_event:
		if event[0]
