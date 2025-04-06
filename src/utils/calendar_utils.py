from icalendar import Calendar, Event

def generate_calendar(schedule):
    cal = Calendar()
    for session in schedule:
        event = Event()
        event.add("summary", session["topic"])
        event.add("description", session["description"])
        event.add("dtstart", session["start_time"])
        event.add("dtend", session["end_time"])
        cal.add_component(event)
    return cal.to_ical()
