class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size=10):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        new_contact = Contact(key, value)

        if self.data[index] is None:
            self.data[index] = Node(key, new_contact)
            return

        current = self.data[index]

        while current is not None:
            if current.key == key:
                current.value.number = value
                return

            if current.next is None:
                break

            current = current.next

        current.next = Node(key, new_contact)

    def search(self, key):
        index = self.hash_function(key)

        current = self.data[index]

        while current is not None:
            if current.key == key:
                return current.value

            current = current.next

        return None

    def print_table(self):
        for i in range(self.size):
            print(f"Index {i}:", end=" ")

            current = self.data[i]

            if current is None:
                print("Empty")
            else:
                while current is not None:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()

# Test your hash table implementation here. 

table = HashTable(10)

#This prints the empty table
table.print_table()

#This adds some values
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")

#This prints the new table structure
table.print_table()

#This searches for a value
contact = table.search("John")
print("\nSearch result:", contact)

table.insert("Amy", "111-222-3333")
table.insert("May", "222-333-1111")

table.print_table()

table.insert("Rebecca", "999-444-9999")

table.print_table()

print(table.search("Chris"))

#Design Memo
#For this assignment I chose to use a hash table because it allows contacts to be stored and found quickly. 
#Instead of searching through every contact one by one, a hash table uses a 
#hash function to calculate where a contact should be stored based on their name. 
#This makes searching much faster, especially when dealing with a large number of contacts. 
#On average inserting and searching for a contact takes O(1) time.
#To handle collisions, I used a method called separate chaining. 
#This means that if two contacts are assigned to the same index in the hash table, 
#they are stored in a linked list at that location. I used my Node class to connect
#contacts together whenever a collision occurs. I also made sure that if a
#contact with the same name is inserted again, their existing phone number
#gets updated instead of creating a duplicate entry.
#An engineer might choose a hash table over a list or tree when they need to
#quickly look up information using a specific key. For example, a contact
#list is a good use for a hash table because people usually search for contacts by name. 
#A regular list would require checking each entry individually, while a tree is useful 
#when data needs to stay organized or sorted. Overall, I think a hash table is a good choice 
#for this project because it makes storing, updating, and searching for contacts efficient.
