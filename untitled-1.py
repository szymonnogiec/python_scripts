def sum(number_one, number_two):
    number_one_int = convert_intiger(number_one)
    number_two_int = convert_intiger(number_two)
    
    result = number_one_int + number_two_int
    
    return result

def convert_intiger(number_string):
    converted_intiger = int(number_string)
    return converted_intiger

answer = sum("1","2")