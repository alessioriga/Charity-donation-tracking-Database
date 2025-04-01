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

def insertNewDonor ():

    connection = db.connect("Alessio_charity_donations.db.db")

    first_name = input("Insert the first name: ")
    surname = input("Insert the surname: ")
    company = input("Insert the company: ")
    postcode = input("Insert the postcode: ")
    address = address_input("Insert the address")
    phone_number = number_input("Insert the phone number")
    email = email_input("Insert the email")

    connection.execute("INSERT INTO Donor (first_name, surname, company, postcode, address, phone_number, email) VALUES (?, ?, ?, ?, ?, ?, ?)", (first_name, surname, company, postcode, address, phone_number, email))
    connection.commit()
    connection.close()

    print("✅ Donor added.")
    time.sleep(2)

def viewDonors ():

    connection = db.connect("Alessio_charity_donations.db")

    print("Donors:\n")
    for row in connection.execute("SELECT * FROM Donor"):
        print(row)

    connection.close()
    time.sleep(2)

def updateDonors ():
    
    connection = db.connect("Alessio_charity_donations.db")

    print("Insert a Donor ID to update.\n")
    donor_id = donorIdInput(connection)
    updated_email = email_input("Insert the new email")

    connection.execute("UPDATE Donor SET email = ? WHERE id = ?", (updated_email, donor_id))

    connection.commit()
    connection.close()

    print("✅ Donor updated.")
    time.sleep(2)

def deleteDonor ():
    connection = db.connect("Alessio_charity_donations.db")
    
    cursor = connection.cursor()

    print("Insert a Donor ID to delete.\n")
    donor_id = donorIdInput(connection)
    if confirmation_input("Are you sure you want to delete Donor ID " + donor_id + "?"):
        if searchDonationByDonorId(connection, donor_id):
            print("❗ This donor ID is being used by a donation.")
        else:
            cursor.execute("DELETE FROM Donor WHERE id = ?", (donor_id))
            connection.commit()
            print("✅ Donor: " + donor_id + " has been deleted.")
        time.sleep(2)
    else:
        print("❌ The Donor hasn't been deleted.")
        time.sleep(2)

def insertNewPaymentMethod ():

    connection = db.connect("Alessio_charity_donations.db")

    method = input_mandatory("Insert the Payment Method: ")

    connection.execute("INSERT INTO PaymentMethod (method) VALUES (?)", (method))
    connection.commit()
    connection.close()

    print("✅ Pyment Method added.")
    time.sleep(2)

def viewPaymentMethods ():

    connection = db.connect("Alessio_charity_donations.db")

    print("Payment Methods:\n")
    for row in connection.execute("SELECT * FROM PaymentMethod"):
        print(row)

    connection.close()
    time.sleep(2)

def updatePaymentMethods ():

    connection = db.connect("Alessio_charity_donations.db")

    print("Insert a Payment Method ID to update.\n")
    paymentMethod_id = paymentMethodIdInput(connection)
    updated_method = input_mandatory("Insert the new Payment Method: ")

    connection.execute("UPDATE PaymentMethod SET method = ? WHERE id = ?", (updated_method, paymentMethod_id))

    connection.commit()
    connection.close()

    print("✅ Payment Method updated.")
    time.sleep(2)

def deletePaymentMethod ():
    connection = db.connect("Alessio_charity_donations.db")
    
    cursor = connection.cursor()

    print("Insert a Payment Method ID to delete.\n")
    paymentMethod_id = paymentMethodIdInput(connection)
    if confirmation_input("Are you sure you want to delete Payment method ID " + paymentMethod_id + "?"):
        if searchDonationByPaymentMethodId(connection, paymentMethod_id):
            print("❗ This payment method ID is being used by a donation.")
        else:
            cursor.execute("DELETE FROM PaymentMethod WHERE id = ?", (paymentMethod_id))
            connection.commit()
            print("✅ Payment Method: " + paymentMethod_id + " has been deleted.")
        time.sleep(2)
    else:
        print("❌ The Payment Method hasn't been deleted.")
        time.sleep(2)