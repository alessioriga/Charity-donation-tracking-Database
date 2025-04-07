import sqlite3 as db
import time

from db.create_tables import *

def insertValue():
    connection =db.connect("Alessio_charity_donations.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys= ON")

    #This command adds values to the Donor table such as (first_name, surname, company, postcode, address, phone_number, email)
    addDonor = """
        INSERT INTO Donor (first_name, surname, company, postcode, address, phone_number, email)
        VALUES
        ('Alessio', 'Rigamonti', 'SaturnTech', 'M47GR', '71 Guide Post Road, Salford', 0758642950, 'alessio.rigamonti@saturntech.com'),
        ('Karima', 'Chakhssi', 'Tesla', 'M58YR', '71 Dalton Street, Manchester', 0759759476, 'karima.chakhssi@tesla.com'),
        ('Javi', 'Clavijo', 'NexusTech', '14013', '4 Calle Libertador, Sivilla', 3457392134, 'javi.clavijo@nexustech.com'),
        ('Inma', 'Castilla', 'Ubisoft', '9008', '19 Fredrik Langes, Tromsø', 3458600044, 'inma.castilla@ubisoft.com')
    """

    #This command adds values to the Event table such as (name, start_date, finish_date, location, cost)
    addEvent = """
        INSERT INTO Event (name, start_date, finish_date, location, cost)
        VALUES
        ('Charity Run 2025', '03-09-2025', '03-09-2025', 'London', 7000.00),
        ('VICE Summer Fest 2025', '07-08-2025', '11-08-2025', 'Bolton', 4000.00),
        ('Cancer Research UK', '23-05-2025', '24-05-2025', 'Manchester', 5000.00),
        ('Macmillan Cancer Support', '27-07-2025', '27-07-2025', 'Belfast', 6000.00)
    """

    #This command adds values to the Payment Method table such as (method)
    addPaymentMethod = """
        INSERT INTO PaymentMethod (method)
        VALUES
        ('Credit Card'),
        ('Cash'),
        ('Bank Transfer')
    """

    #This command adds values to the Volunteer table such as (first_name, surname, postcode, address, phone_number, email, event_id)
    addVolunteer = """
        INSERT INTO Volunteer (first_name, surname, postcode, address, phone_number, email, event_id)
        VALUES
        ('Patricia', 'Shannon', 'HG12DR', '3  Coppice Gate, Harrogate', 0799431870, 'patricia.shannon@email.com', 1),
        ('Lyle', 'Todd', 'BN31FA', '99 Western Road, Hove', 0752900762, 'lyle.todd@email.com', 4),
        ('Jere', 'Schwartz', 'DD21AT', '209 Perth Road, Dundee', 0718375699, 'jere.schwartz@email.com', 2),
        ('Danielle', 'Lester', 'NE1TL', '28 Jasmine Ave, Newcastle', 0713958559, 'danielle.lester@email.com', 3)
    """

    #This command adds values to the Donation table such as (amount_donated, date, notes, donor_id, event_id, volunteer_id, payment_method_id)
    addDonation = """
        INSERT INTO Donation (amount_donated, date, notes, donor_id, event_id, volunteer_id, payment_method_id)
        VALUES
        (350.00, '03-09-2025', 'Charity donation', 1, 1, 1, 2),
        (750.00, '08-08-2025', 'Tesla team donation', 2, 2, 2, 3),
        (100.00, '23-05-2025', 'Inma Castilla donation', 4, 3, 3, 3),
        (150.00, '27-07-2025', 'Donation to Cancer Research', 3, 4, 4, 1)
    """
    
    cursor.execute(addDonor)
    cursor.execute(addEvent)
    cursor.execute(addPaymentMethod)
    cursor.execute(addVolunteer)
    cursor.execute(addDonation)

    connection.commit()
    connection.close()
    print("✅ Data added successfully.")
    time.sleep(2)
