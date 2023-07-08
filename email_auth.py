import re

email = input("Please enter your email address: ")

pattern = r"[\w\.-]+@[\w\.-]+\.\w{2,3}"

if re.search(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")
