import sqlite3 as db

def createTable ():
    connection = db.connect("Alessio_charity_donations.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys= ON")
    
    # Donor Table
    donorTable = """
        CREATE TABLE IF NOT EXISTS Donor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        surname TEXT,
        company TEXT,
        postcode TEXT,
        address TEXT,
        phone_number INTEGER,
        email TEXT
        )
    """

    # Volunteer Table
    volunteerTable = """
        CREATE TABLE IF NOT EXISTS Volunteer (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        surname TEXT NOT NULL,
        postcode TEXT NOT NULL,
        address TEXT NOT NULL,
        phone_number INTEGER,
        email TEXT,
        event_id INTEGER NOT NULL,
        FOREIGN KEY (event_id) REFERENCES Event(id)
        )
    """

    # Event Table
    eventTable = """
        CREATE TABLE IF NOT EXISTS Event (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        start_date TEXT NOT NULL,
        finish_date TEXT,
        location TEXT NOT NULL,
        cost REAL NOT NULL
        )
    """

    # Payment Method Table
    paymentMethodTable = """
        CREATE TABLE IF NOT EXISTS PaymentMethod (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        method TEXT NOT NULL
        )
    """

    # Donation Table
    donationTable = """
        CREATE TABLE IF NOT EXISTS Donation (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount_donated REAL NOT NULL,
        date TEXT NOT NULL,
        notes TEXT,
        donor_id INTEGER NOT NULL,
        event_id INTEGER NOT NULL,
        volunteer_id INTEGER,
        payment_method_id INTEGER NOT NULL,
        FOREIGN KEY (donor_id) REFERENCES Donor(id) ON DELETE RESTRICT,
        FOREIGN KEY (event_id) REFERENCES Event(id) ON DELETE RESTRICT, 
        FOREIGN KEY (volunteer_id) REFERENCES Volunteer(id) ON DELETE RESTRICT,
        FOREIGN KEY (payment_method_id) REFERENCES PaymentMethod(id) ON DELETE RESTRICT
        )
    """

    cursor.execute(donorTable)
    cursor.execute(volunteerTable)
    cursor.execute(eventTable)
    cursor.execute(paymentMethodTable)
    cursor.execute(donationTable)

    connection.commit()
    connection.close()
    print("✅ Tables created successfully.")