def to_decimal(number_string, original_base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_string = number_string.upper() 
    total_value = 0
    power = 0

    for char in number_string[::-1]:
        char_value = digits.index(char)
        total_value += char_value * (original_base ** power)
        power += 1
    return total_value

def from_decimal(decimal_number, target_base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if decimal_number == 0:
        return "0"
    
    result_string = ""

    while decimal_number > 0:
        remainder = decimal_number % target_base
        decimal_number = decimal_number // target_base
        char_to_add = digits[remainder]
        result_string = char_to_add + result_string

    return result_string