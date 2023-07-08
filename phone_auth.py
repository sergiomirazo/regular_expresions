import re

phone = input("Please enter a phone number with the format xxx-xxx-xxxx: ")
phone_num_pattern1 = re.compile(r'\d{3}-\d{3}-\d{4}')
phone_num_pattern2 = re.compile(r'\d{3} \d{3} \d{4}')

match1 = phone_num_pattern1.search(phone)
match2 = phone_num_pattern2.search(phone)

if match1 or match2:
    print("Phone number is valid!")
else:
    print("Phone number is invalid!")
