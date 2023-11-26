from abc import ABC,abstractmethod

# Abstract class for inputs 
class AddressBookInputs(ABC):
    @abstractmethod
    def add_address_book_input(self):
        pass

# Taking necessary inputs, if needed extra inputs
# we can extend it without making modifications to already existing classes
class FirstNameInput(AddressBookInputs):
    def add_address_book_input(self):
        first_name = input("Enter your first name : ")
        return first_name

class LastNameInput(AddressBookInputs):
    def add_address_book_input(self):
        last_name = input("Enter your last name : ")
        return last_name

class AddressInput(AddressBookInputs):
    def add_address_book_input(self):
        address = input("Enter your address details : ")
        return address
        
class PhoneInput(AddressBookInputs): 
    def add_address_book_input(self):
        phone = input("Enter your phone number : ")
        return phone


# Class for the address
class AddressBook:
    
    # Class variables for storing all the addresses
    address_by_name = {}
    address_by_phone = {}
    
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.address = None
        self.phone = None
    
    # Taking input for address book
    def inputs(self):
        self.first_name = FirstNameInput().add_address_book_input()
        self.last_name = LastNameInput().add_address_book_input()
        self.address = AddressInput().add_address_book_input()
        self.phone = PhoneInput().add_address_book_input()
    
    # Storing input in address book
    def add_in_address_book(self):
        AddressBook.address_by_phone[self.phone] = {"First_name": self.first_name,"Last_name": self.last_name, "Address": self.address, "Phone": self.phone}
        AddressBook.address_by_name[f"{self.first_name} {self.last_name}"] = {"First_name": self.first_name,"Last_name": self.last_name, "Address": self.address, "Phone": self.phone}
        print("Successfully added in address book")
        
class Client:
    def __init__(self, address_book):
        self.address_book = address_book
    
    def add_address(self):
        # Taking input
        self.address_book.inputs()
        # Add address in the book
        self.address_book.add_in_address_book()
        

if __name__ == "__main__":
    address_book_input = AddressBook()
    client = Client(address_book_input)
    
    client.add_address()
    
    

        