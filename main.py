
#Strings
message="flower"
print(message[0])

#multiline String
paragraph = """
This is a random string with
multiple lines
in it

Five Lines....
"""
print(paragraph)

#Formatting String Placeholders
hello_message= "My name is {0} {1}, i'm {2} right now!".format("D","G","Happy")
print(hello_message)

#Obtaining user input
#print("Enter Your name")
name=input("Enter Your Name: ")
print("Hello {}".format(name))