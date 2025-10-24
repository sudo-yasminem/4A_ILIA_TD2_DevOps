import raclette

begin_date = "20/01/2020"
time_event = 30
name = "Session Raclette"
event = {}
tab_event = [event]

def test_createEvents():
	assert raclette.createEvents(begin_date, time_event ,name) == (1579474800.0, 30, "Session Raclette")
		
def test_Get_events():
	assert raclette.Get_events() == []
	
def test_add(): 
	assert raclette.add_events(event,[]) == [{}]

def test_first_event(tab_event):
	assert raclette.first_event([]) = tab_event[0]

#A finir