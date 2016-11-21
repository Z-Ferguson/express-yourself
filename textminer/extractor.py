import re


def phone_numbers(text):
    b = re.findall(r'\(\d{3}\)\s\d{3}\-\d{4}', text)
    return b
