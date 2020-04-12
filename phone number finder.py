import re

phoneNumber_regex = re.compile(r'\d\d\d\d\d\d\d\d\d\d')

number= phoneNumber_regex.search(input("enter the text --> "))
print("phone number in text is ",number.group())

