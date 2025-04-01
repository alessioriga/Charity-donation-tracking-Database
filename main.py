from db.create_tables import *
from db.insert_values import *
from db.repository import *

def main_menu():
    while True:
        print("\n🌟 Charity Donation Tracking 🌟")
        print("1. Add Donor")
        print("2. View Donors")
        print("3. Update Donor")
        print("4. Delete Donor")
        print("5. Add Volunteer")
        print("6. View Volunteers")
        print("7. Update Volunteer")
        print("8. Delete Volunteer")
        print("9. Add Event")
        print("10. View Events")
        print("11. Update Event")
        print("12. Delete Event")
        print("13. Add Donation")
        print("14. View Donations")
        print("15. Update Donation")
        print("16. Delete Donation")
        print("17. Search Donations by Donor")
        print("18. Search Donations by Event")
        print("19. Search Donations by Volunteer")
        print("20. Add Payment Method")
        print("21. View Payment Methods")
        print("22. Update Payment Method")
        print("23. Delete Payment Method")

        print("0. Exit")
        choice = input("Choose an option: ")

        actions = {
            "1": insertNewDonor,
            "2": viewDonors,
            "3": updateDonors,
            "4": deleteDonor,
            "5": insertNewVolunteer,
            "6": viewVolunteers,
            "7": updateVolunteers,
            "8": deleteVolunteer,
            "9": insertNewEvent,
            "10": viewEvents,
            "11": updateEvents,
            "12": deleteEvent,
            "13": insertNewDonation,
            "14": viewDonations,
            "15": updateDonations,
            "16": deleteDonation,
            "17": searchDonationByDonor,
            "18": searchDonationByEvent,
            "19": searchDonationByVolunteer,
            "20": insertNewPaymentMethod,
            "21": viewPaymentMethods,
            "22": updatePaymentMethods,
            "23": deletePaymentMethod,
            "0": exit
        }

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()
    createTable()
    insertValue()
    