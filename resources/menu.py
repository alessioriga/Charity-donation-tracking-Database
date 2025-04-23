from db.repository import *

def main_menu():
    while True:
        print("\n🌟 Charity Donation Tracking 🌟")
        print("1. Add data")
        print("2. View data")
        print("3. Update data")
        print("4. Delete data")
        print("0. Exit")
        choice = input("Choose an option: ")
        print("")

        actions = {
            "1": addData,
            "2": viewData,
            "3": updateData,
            "4": deleteData,
            "0": exit
        }

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid option.")

def addData():
    print("1. Add Donor")
    print("2. Add Volunteer")
    print("3. Add Event")
    print("4. Add Donation")
    print("5. Add Payment Method")
    print("0. Back")
    choice = input("Choose an option: ")
    print("")

    actions = {
        "1": insertNewDonor,
        "2": insertNewVolunteer,
        "3": insertNewEvent,
        "4": insertNewDonation,
        "5": insertNewPaymentMethod,
        "0": main_menu
    }

    action = actions.get(choice)
    if action:
        action()
    else:
        print("Invalid option.")

def viewData():
    print("1. View Donors")
    print("2. View Volunteers")
    print("3. View Events")
    print("4. View Donations")
    print("5. Search Donations by Donor")
    print("6. Search Donations by Event")
    print("7. Search Donations by Volunteer")
    print("8. View Payment Methods")
    print("0. Back")
    choice = input("Choose an option: ")
    print("")

    actions = {
        "1": viewDonors,
        "2": viewVolunteers,
        "3": viewEvents,
        "4": viewDonations,
        "5": searchDonationByDonor,
        "6": searchDonationByEvent,
        "7": searchDonationByVolunteer,
        "8": viewPaymentMethods,
        "0": main_menu
    }

    action = actions.get(choice)
    if action:
        action()
    else:
        print("Invalid option.")

def updateData():
    print("1. Update Donor")
    print("2. Update Volunteer")
    print("3. Update Event")
    print("4. Update Donation")
    print("5. Update Payment Method")
    print("0. Back")
    choice = input("Choose an option: ")
    print("")

    actions = {
        "1": updateDonors,
        "2": updateVolunteers,
        "3": updateEvents,
        "4": updateDonations,
        "5": updatePaymentMethods,
        "0": main_menu
    }

    action = actions.get(choice)
    if action:
        action()
    else:
        print("Invalid option.")

def deleteData():
    print("1. Delete Donor")
    print("2. Delete Volunteer")
    print("3. Delete Event")
    print("4. Delete Donation")
    print("5. Delete Payment Method")
    print("0. Exit")
    choice = input("Choose an option: ")
    print("")

    actions = {
        "1": deleteDonor,
        "2": deleteVolunteer,
        "3": deleteEvent,
        "4": deleteDonation,
        "5": deletePaymentMethod,
        "0": main_menu
    }

    action = actions.get(choice)
    if action:
        action()
    else:
        print("Invalid option.")
