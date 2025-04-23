import sqlite3 as db

from resources.utils import *
from db.resources.dbUtils import *
from datetime import datetime

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

def viewEvents ():

    connection = db.connect("Alessio_charity_donations.db")

    print("Events:\n")
    for row in connection.execute("SELECT * FROM Event"):
        print(row)

    connection.close()

def updateEvents ():

    connection = db.connect("Alessio_charity_donations.db")

    print("Insert an Event ID to update.\n")
    event_id = eventIdInput(connection)
    updated_cost = amount_input_mandatory("Insert the new cost: £")
    connection.execute("UPDATE Event SET cost = ? WHERE id = ?", (updated_cost, event_id))

    connection.commit()
    connection.close()

    print("✅ Event updated.")

def deleteEvent ():

    connection = db.connect("Alessio_charity_donations.db")
    
    cursor = connection.cursor()

    print("Insert a Event ID to delete.\n")
    eventId = eventIdInput(connection)
    if confirmation_input("Are you sure you want to delete Event ID " + eventId + "?"):
        
        if searchById(connection, "Donation", "event_id", eventId):
            print("❗ This event ID is being used by a donation.")
        
        elif searchById(connection, "Volunteer", "event_id", eventId):
            print("❗ This event ID is being used by a volunteer.")
        else:
            cursor.execute("DELETE FROM Event WHERE id = ?", (eventId))
            connection.commit()
            print("✅ Event: " + eventId + " has been deleted.")
    else:
        print("❌ The Event hasn't been deleted.")

def insertNewDonor ():

    connection = db.connect("Alessio_charity_donations.db")

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

def viewDonors ():

    connection = db.connect("Alessio_charity_donations.db")

    print("Donors:\n")
    for row in connection.execute("SELECT * FROM Donor"):
        print(row)

    connection.close()

def updateDonors ():
    
    connection = db.connect("Alessio_charity_donations.db")

    print("Insert a Donor ID to update.\n")
    donor_id = donorIdInput(connection)
    updated_email = email_input("Insert the new email")

    connection.execute("UPDATE Donor SET email = ? WHERE id = ?", (updated_email, donor_id))

    connection.commit()
    connection.close()

    print("✅ Donor updated.")

def deleteDonor ():

    connection = db.connect("Alessio_charity_donations.db")
    
    cursor = connection.cursor()

    print("Insert a Donor ID to delete.\n")
    donor_id = donorIdInput(connection)
    if confirmation_input("Are you sure you want to delete Donor ID " + donor_id + "?"):
        
        if searchById(connection, "Donation", "donor_id", donor_id):
            print("❗ This donor ID is being used by a donation.")
        else:
            cursor.execute("DELETE FROM Donor WHERE id = ?", (donor_id))
            connection.commit()
            print("✅ Donor: " + donor_id + " has been deleted.")
    else:
        print("❌ The Donor hasn't been deleted.")

def insertNewPaymentMethod ():

    connection = db.connect("Alessio_charity_donations.db")

    method = input_mandatory("Insert the Payment Method: ")

    connection.execute("INSERT INTO PaymentMethod (method) VALUES (?)", (method))
    connection.commit()
    connection.close()

    print("✅ Payment Method added.")

def viewPaymentMethods ():

    connection = db.connect("Alessio_charity_donations.db")

    print("Payment Methods:\n")
    for row in connection.execute("SELECT * FROM PaymentMethod"):
        print(row)

    connection.close()

def updatePaymentMethods ():

    connection = db.connect("Alessio_charity_donations.db")

    print("Insert a Payment Method ID to update.\n")
    paymentMethod_id = paymentMethodIdInput(connection)
    updated_method = input_mandatory("Insert the new Payment Method: ")

    connection.execute("UPDATE PaymentMethod SET method = ? WHERE id = ?", (updated_method, paymentMethod_id))

    connection.commit()
    connection.close()

    print("✅ Payment Method updated.")

def deletePaymentMethod ():

    connection = db.connect("Alessio_charity_donations.db")
    
    cursor = connection.cursor()

    print("Insert a Payment Method ID to delete.\n")
    paymentMethod_id = paymentMethodIdInput(connection)
    if confirmation_input("Are you sure you want to delete Payment method ID " + paymentMethod_id + "?"):
        
        if searchById(connection, "Donation", "payment_method_id", paymentMethod_id):
            print("❗ This payment method ID is being used by a donation.")
        else:
            cursor.execute("DELETE FROM PaymentMethod WHERE id = ?", (paymentMethod_id))
            connection.commit()
            print("✅ Payment Method: " + paymentMethod_id + " has been deleted.")
    else:
        print("❌ The Payment Method hasn't been deleted.")

def insertNewDonation ():

    connection = db.connect("Alessio_charity_donations.db")
    
    amount_donated = amount_input_mandatory("Please enter the amount: £")
    
    date = datetime.now().strftime("%d-%m-%Y")
    notes = input("Insert a note: ")
    donor_id = donorIdInput(connection)
    event_id = eventIdInput(connection)
    volunteer_id = volunteerIdInput(connection)
    payment_method_id = paymentMethodIdInput(connection)

    connection.execute("INSERT INTO Donation (amount_donated, date, notes, donor_id, event_id, volunteer_id, payment_method_id) VALUES (?, ?, ?, ?, ?, ?, ?)", (amount_donated, date, notes, donor_id, event_id, volunteer_id, payment_method_id))
    connection.commit()
    connection.close()

    print("✅ Donation added.")
    print(f"Thank you!!! You donated £{amount_donated:.2f}")

def viewDonations ():

    connection = db.connect("Alessio_charity_donations.db")

    print("Donations:\n")
    for row in connection.execute("SELECT * FROM Donation"):
        print(row)

    connection.close()

def updateDonations ():

    connection = db.connect("Alessio_charity_donations.db")

    print("Insert a Donation ID to update.\n")
    donation_id = donationIdInput (connection)
    updated_amount = amount_input_mandatory("Please enter the new amount: £")

    connection.execute("UPDATE Donation SET amount_donated = ? WHERE id = ?", (updated_amount, donation_id))

    connection.commit()
    connection.close()

    print("✅ Donation updated.")
    print(f"Thank you!!! You donated £{updated_amount:.2f}")

def deleteDonation ():

    connection = db.connect("Alessio_charity_donations.db")

    cursor = connection.cursor()

    print("Insert a Donation ID to delete.\n")
    donation_id = donationIdInput(connection)
    if confirmation_input("Are you sure you want to delete Donation ID " + donation_id + "?"):
        cursor.execute("DELETE FROM Donation WHERE id = ?", (donation_id))
        connection.commit()
        print("✅ Donation: " + donation_id + " has been deleted.")
    else:
        print("❌ The Donation hasn't been deleted.")

def searchDonationByDonor ():

    connection = db.connect("Alessio_charity_donations.db")

    cursor = connection.cursor()

    print("Insert the Donor ID to view past donations.\n")
    donor_id = donorIdInput(connection)

    cursor.execute("SELECT id, amount_donated, date, notes, event_id, volunteer_id, payment_method_id FROM Donation WHERE donor_id = ?", (donor_id,))
    results = cursor.fetchall()

    if results:
        print("Donations for Donor ID " + donor_id + ":")
        for row in results:
            print(f"Donation ID: {row[0]}, Amount: £{row[1]:.2f}, Date: {row[2]}")
            print(f"    Event ID: {row[4]}, Volunteer ID: {row[5]}, Payment Method ID: {row[6]}")
            if row[3]:
                print(f"    Notes: {row[3]}")
    else:
        print("❌ No donations found for this donor.")
    
    connection.close()

def searchDonationByVolunteer ():

    connection = db.connect("Alessio_charity_donations.db")

    cursor = connection.cursor()

    print("Insert the Volunteer ID to view past donations.\n")
    volunteer_id = volunteerIdInput(connection)

    cursor.execute("SELECT id, amount_donated, date, notes, donor_id, event_id, payment_method_id FROM Donation WHERE volunteer_id = ?", (volunteer_id,))
    results = cursor.fetchall()

    if results:
        print("Donations for  ID " + volunteer_id + ":")
        for row in results:
            print(f"Donation ID: {row[0]}, Amount: £{row[1]:.2f}, Date: {row[2]}")
            print(f"    Donor ID: {row[4]}, Event ID: {row[5]}, Payment Method ID: {row[6]}")
            if row[3]:
                print(f"    Notes: {row[3]}")
    else:
        print("❌ No donations found for this volunteer.")
    
    connection.close()

def searchDonationByEvent ():

    connection = db.connect("Alessio_charity_donations.db")

    cursor = connection.cursor()

    print("Insert the Event ID to view past donations.\n")
    event_id = eventIdInput(connection)

    cursor.execute("SELECT id, amount_donated, date, notes, donor_id, volunteer_id, payment_method_id FROM Donation WHERE event_id = ?", (event_id,))
    results = cursor.fetchall()

    if results:
        print("Donations for  ID " + event_id + ":")
        for row in results:
            print(f"Donation ID: {row[0]}, Amount: £{row[1]:.2f}, Date: {row[2]}")
            print(f"    Donor ID: {row[4]}, Volunteer ID: {row[5]}, Payment Method ID: {row[6]}")
            if row[3]:
                print(f"    Notes: {row[3]}")
    else:
        print("❌ No donations found for this event.")
    
    connection.close()

def insertNewVolunteer ():

    connection = db.connect("Alessio_charity_donations.db")

    first_name = input_mandatory("Insert the first name: ")
    surname = input_mandatory("Insert the surname: ")
    postcode = input_mandatory("Insert the postcode: ")
    address = address_input("Insert the address")
    phone_number = number_input("Insert the phone number")
    email = email_input("Insert the email: ")
    event_id = eventIdInput(connection)

    connection.execute("INSERT INTO Volunteer (first_name, surname, postcode, address, phone_number, email, event_id) VALUES (?, ?, ?, ?, ?, ?, ?)", (first_name, surname, postcode, address, phone_number, email, event_id))
    connection.commit()
    connection.close()

    print("✅ Volunteer added.")

def viewVolunteers ():

    connection = db.connect("Alessio_charity_donations.db")

    print("Volunteers:\n")
    for row in connection.execute("SELECT * FROM Volunteer"):
        print(row)

    connection.close()

def updateVolunteers ():

    connection = db.connect("Alessio_charity_donations.db")

    print("Insert a Volunteer ID to update.\n")
    volunteer_id = volunteerIdInput (connection)
    updated_phone_number = number_input("Insert the new phone number")

    connection.execute("UPDATE Volunteer SET phone_number = ? WHERE id = ?", (updated_phone_number, volunteer_id))

    connection.commit()
    connection.close()

    print("✅ Volunteer updated.")

def deleteVolunteer ():
    
    connection = db.connect("Alessio_charity_donations.db")
    
    cursor = connection.cursor()

    print("Insert a Volunteer ID to delete.\n")
    volunteer_id = volunteerIdInput(connection)
    if confirmation_input("Are you sure you want to delete Volunteer ID " + volunteer_id + "?"):

        if searchById(connection, "Donation", "volunteer_id", volunteer_id):
            print("❗ This volunteer ID is being used by a donation.")
        else:
            cursor.execute("DELETE FROM Volunteer WHERE id = ?", (volunteer_id))
            connection.commit()
            print("✅ Volunteer: " + volunteer_id + " has been deleted.")
    else:
        print("❌ The Volunteer hasn't been deleted.")
