from resources.utils import *

def donorIdInput (connection):

    print("ID, Name Surname")
    for row in connection.execute("SELECT id, first_name, surname FROM Donor"):
        print(str(row[0]) + ", " + row[1] + " " + row[2])

    while True:
        user_input = input("Please enter an existing Donor ID: ")

        cursor = connection.execute("SELECT * FROM Donor WHERE id = ? ", (user_input,))
        row = cursor.fetchone()

        if row:
            return user_input
        else:
            print("❌ ID not found. Try again.")

def eventIdInput (connection):

    print("ID, Event")
    for row in connection.execute("SELECT id, name FROM Event"):
        print(str(row[0]) + ", " + row[1])

    while True:
        user_input = input("❗ Please enter an existing Event ID: ")

        cursor = connection.execute("SELECT * FROM Event WHERE id = ? ", (user_input,))
        row = cursor.fetchone()

        if row:
            return user_input
        else:
            print("❌ ID not found. Try again.")

def volunteerIdInput (connection):

    print("ID, Volunteer")
    for row in connection.execute("SELECT id, first_name, surname FROM Volunteer"):
        print(str(row[0]) + ", " + row[1] + " " + row[2]) 

    while True:
        user_input = input("❗ Please enter an existing Volunteer ID: ")
        if user_input == "":
            return user_input
        cursor = connection.execute("SELECT * FROM Volunteer WHERE id = ? ", (user_input,))
        row = cursor.fetchone()

        if row:
            return user_input
        else:
            print("❌ ID not found. Try again.")

def paymentMethodIdInput (connection):

    print("ID, Payment Method")
    for row in connection.execute("SELECT id, method FROM PaymentMethod"):
        print(str(row[0]) + ", " + row[1])

    while True:
        user_input = input("❗ Please enter an existing Payment Method ID: ")

        cursor = connection.execute("SELECT * FROM PaymentMethod WHERE id = ? ", (user_input,))
        row = cursor.fetchone()

        if row:
            return user_input
        else:
            print("❌ ID not found. Try again.")

def donationIdInput (connection):

    print("ID, Donation")
    for row in connection.execute("SELECT id, date FROM Donation"):
        print(str(row[0]) + ", " + row[1])

    while True:
        user_input = input("❗ Please enter an existing Donation ID: ")

        cursor = connection.execute("SELECT * FROM Donation WHERE id = ?", (user_input,))
        row = cursor.fetchone()

        if row:
            return user_input
        else:
            print("❌ ID not found. Try again.")

def searchDonationByPaymentMethodId (connection, paymentMethodId):

    cursor = connection.execute("SELECT * FROM Donation WHERE payment_method_id = ? ", (paymentMethodId))

    # This method returns true if fetchone returns a row and false if not. So basically if there is data the function returns True and False otherwise.
    return cursor.fetchone() != None

def searchDonationByEventId(connection, eventId):

    cursor = connection.execute("SELECT * FROM Donation WHERE event_id = ? ", (eventId))

    # This method returns true if fetchone returns a row and false if not. So basically if there is data the function returns True and False otherwise.
    return cursor.fetchone() != None

def searchVolunteerByEventId(connection, eventId):

    cursor = connection.execute("SELECT * FROM Volunteer WHERE event_id = ? ", (eventId))

    # This method returns true if fetchone returns a row and false if not. So basically if there is data the function returns True and False otherwise.
    return cursor.fetchone() != None

def searchDonationByDonorId (connection, donorId):

    cursor = connection.execute("SELECT * FROM Donation WHERE donor_id = ? ", (donorId))

    # This method returns true if fetchone returns a row and false if not. So basically if there is data the function returns True and False otherwise.
    return cursor.fetchone() != None

def searchDonationByVolunteerId (connection, volunteerId):

    cursor = connection.execute("SELECT * FROM Donation WHERE volunteer_id = ? ", (volunteerId))

    # This method returns true if fetchone returns a row and false if not. So basically if there is data the function returns True and False otherwise.
    return cursor.fetchone() != None
