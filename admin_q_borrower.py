import string_utils
import updateProcedures
import fetchProcedures
import addProcedures
import deleteProcedures

def start(self):
    print("What would you like to do?\n")
    self.choice = input("1) Add Borrower\n2) Update Borrower\n3) Delete Borrower\n")
    if self.choice == "1":
        add_borrower(self)
    elif self.choice == "2":
        update_borrower(self)
    elif self.choice == "3":
        delete_borrower(self)
    else:
        print("Must enter a valid option (ie 1, 2, 3)")
        start(self)

def add_borrower(self):
    self.store["name"] = input("What is the name of your new borrower\n")
    self.store["address"] = input("What's the address of your borrower\n")
    self.store["phone"] = input("Lastly, what is the phone number of your borrower\n")
    addProcedures.addBorrower(self.store["name"],self.store["address"],self.store["phone"])

def update_borrower(self):
    borrowerList=fetchProcedures.fetchBorrowers()
    borrowers = string_utils.display_input_options(borrowerList)
    borrowerChoice=input(borrowers+" Enter borrower card # you want to update?\n")
    bNewName=input("Enter the borrowers new name.\n")
    bNewAddress=input("Enter "+bNewName+" new address.\n")
    bNewPhone=input("Enter "+bNewName+" new phone number. \n")
    updateProcedures.updateBorrowerInfo(borrowerChoice,bNewName,bNewAddress,bNewPhone)
    print("Updating Borrower")

def delete_borrower(self):
    borrowerList=fetchProcedures.fetchBorrowers()
    borrowers = string_utils.display_input_options(borrowerList)
    borrowerChoice=input(borrowers+" Enter borrower card # you want to delete?\n")
    deleteProcedures.deleteBorrower(borrowerChoice)
    print("Deleting Borrower")