import string_utils
import updateProcedures
import fetchProcedures
import addProcedures
import deleteProcedures

def start(self):
    print("What would you like to do?\n")
    self.choice = input("1) Add Library Branch\n2) Update Library Branch\n3) Delete Library Branch\n")
    if self.choice == "1":
        add_library(self)
    elif self.choice == "2":
        update_library(self)
    elif self.choice == "3":
        delete_library(self)
    else:
        print("Must enter a valid option (ie 1, 2, 3)")
        start(self)

def add_library(self):
    newBranchName=input("What do you want to call this new branch?\n")
    newBranchAddress=input("What is the address for the new branch "+newBranchName+"?\n")
    addProcedures.addBranch(newBranchName,newBranchAddress)
    print("Adding Library Branch")

def update_library(self):
    branchList=fetchProcedures.fetchBranchs()
    branches = string_utils.display_input_options(branchList)
    branchChoice = input(branches + "Which branch do you want to update?\n")
    branchChoiceName=(''.join(branchList[int(branchChoice)-1]))
    branchId=fetchProcedures.fetchBranchIdByName(branchChoiceName)
    newBranchName = input("What is the new branch name?\n")
    newBranchAddress = input("What is the new address for "+newBranchName +"?\n")
    updateProcedures.updateBranchInfo(newBranchName,newBranchAddress,branchId[0])
    print("library branch updated")
    # UPDATE LIBRARY BY ID (branchName, branchAddress)
    updateProcedures.updateBranchInfo(newBranchName,newBranchAddress,branchId)

def delete_library(self):
    libraries = fetchProcedures.fetchLibraries()
    libraries = string_utils.build_input_options(self, libraries)
    self.choice = input("Which library would you like to delete?\n" + libraries)
    self.store["branchId"] = self.grabId()
    # DELETE LIBRARY BY ID (branchId)
