import sqlite3 as db
from resources.utils import *
from db.resources.dbUtils import *
from datetime import datetime
import time

def insertNewEvent ():

    connection = db.connect("Alessio_charity_donations.db")

    name = input_mandatory("Insert the Event name: ")
    start_date = date_input_mandatory("Insert a start date")
    finish_date = date_input("Insert a finish date")
    location = input_mandatory("Insert the Event location: ")
    cost = amount_input_mandatory("Insert the Event cost: ")

    connection.execute("INSERT INTO Event (name, start_date, finish_date, location, cost) VALUES (?, ?, ?, ?, ?)", (name, start_date, finish_date, location, cost))
    connection.commit()
    connection.close()
        
    print("✅ Event added.")
    time.sleep(2)

def viewEvents ():

    connection = db.connect("Alessio_charity_donations.db")

    print("Events:\n")
    for row in connection.execute("SELECT * FROM Event"):
        print(row)

    connection.close()
    time.sleep(2)

def updateEvents ():

    connection = db.connect("Alessio_charity_donations.db")

    print("Insert an Event ID to update.\n")
    event_id = eventIdInput(connection)
    updated_cost = amount_input_mandatory("Insert the new cost: £")
    connection.execute("UPDATE Event SET cost = ? WHERE id = ?", (updated_cost, event_id))

    connection.commit()
    connection.close()

    print("✅ Event updated.")
    time.sleep(2)

def deleteEvent ():
    connection = db.connect("Alessio_charity_donations.db")
    
    cursor = connection.cursor()

    print("Insert a Event ID to delete.\n")
    eventId = eventIdInput(connection)
    if confirmation_input("Are you sure you want to delete Event ID " + eventId + "?"):
        if searchDonationByEventId(connection, eventId):
            print("❗ This event ID is being used by a donation.")
        elif searchVolunteerByEventId(connection, eventId):
            print("❗ This event ID is being used by a volunteer.")
        else:
            cursor.execute("DELETE FROM Event WHERE id = ?", (eventId))
            connection.commit()
            print("✅ Event: " + eventId + " has been deleted.")
        time.sleep(2)
    else:
        print("❌ The Event hasn't been deleted.")
        time.sleep(2)

