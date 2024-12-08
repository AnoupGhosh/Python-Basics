numbers = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

phone_number = input("Phone: ")
phone_number_word = ""
for number in phone_number:
    phone_number_word = phone_number_word + numbers[number] + " "

print(phone_number_word)
