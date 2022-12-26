def format_name(first_name, last_name):
    if first_name == "" and last_name == "":
        return "Name: " + first_name + last_name
    elif first_name == "":
        return "Name: " + last_name
    elif last_name == "":
        return "Name: " + first_name
    else:
        return "Name: " + last_name + ", " + first_name

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string

def sum(x, y):
    return(x+y)
print(sum(sum(1,2), sum(3,4)))



print((10 >= 5*2) and (10 <= 5*2))

def fractional_part(numerator, denominator):
    # Check for division by zero
    if denominator == 0:
        return 0
    # Calculate the quotient and get the remainder
    quotient, remainder = divmod(numerator, denominator)
    # Return the remainder divided by the denominator
    return remainder / denominator

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0


