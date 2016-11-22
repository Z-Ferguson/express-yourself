import re


def words(text):
    expected = []
    input = re.findall(r'\w*[^\s][a-zA-Z]+|[a-zA-Z]+', text)
    if input == expected:
        return None
    return input


def phone_number(pn):
    number_dict = {}
    try:
        area_code, part_1, part_2 = re.match(
            r'^\(*(\d{3})\)*[-|\s|\.]*(\d{3})[-|\s|\.]*(\d{4})', pn).groups()
        number_dict["area_code"] = area_code
        number_dict["number"] = "{}-{}".format(part_1, part_2)
        return number_dict
    except:
        return None


def money(c_string):
    money_dict = {}
    try:
        groups = re.match(r'^(\D)(\d+(,\d{3})*(\.\d{2})?)$', c_string).groups()
        money_dict["currency"] = groups[0]
        money_dict["amount"] = float(re.sub(r',', '', groups[1]))
        return money_dict
    except:
        return None
