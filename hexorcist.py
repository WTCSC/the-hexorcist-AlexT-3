from hex_functions import from_decimal, to_decimal

#-------Main Program-------

print("Welcome to HEXORCIST: The universal base converter")

number_string = input("Enter your number (e.g., C7): ")
original_base = int(input("Enter the original base (2–36): "))
target_base = int(input("Enter the target base (2–36): "))

decimal_value = to_decimal(number_string, original_base)
converted_value = from_decimal(decimal_value, target_base)

print(f"\n{number_string} (base {original_base}) = {converted_value} (base {target_base})")