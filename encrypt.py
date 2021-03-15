key = int(input("What's the key? "))
message = input("What's the message? ")

def message_to_numbers(message):
    split_text = [char for char in message]

    number_message = []
    for each in split_text:
        num = ord(each)
        number_message.append(num)

    return number_message

message = message_to_numbers(message)
# print(message)

# functions that make the values, all arbitrary math
def first_value(key, num_1, num_2, num_3):
    value_1 = num_1

    for _ in range(key):
        value_1 += num_2
    
    return value_1 + num_3 * key

def second_value(key, num_1, num_2, num_3):
    value_2 = num_1 + key
    
    for _ in range(num_3):
        value_2 += num_2 + key
        value_2 -= key
    
    return value_2

def third_value(key, num_1, num_2):
    return key * num_1 + (num_2 - key * 3)

output = ''

for each in message:
    value_1 = first_value(key, 5, 2, 12)
    value_2 = second_value(key, 3, 4, 11)
    value_3 = third_value(key, 3, 2)

    # print((each + value_2) * value_1 / value_3)

    output += chr(round(((each + value_2) * value_1) / value_3))
    key += 1

# print(value_1)
# print(value_2)
# print(value_3)

print('encrypted text: ' + output)