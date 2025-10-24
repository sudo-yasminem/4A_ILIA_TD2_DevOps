import calendrier

begin_date = "20/01/2020"
time_event = 30
name = "Session Raclette"

def test_createEvents():
	assert calendrier.createEvents(begin_date, time_event ,name) == (1579474800.0, 30, "Session Raclette")
	

