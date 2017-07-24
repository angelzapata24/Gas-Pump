import gas_pump_core

def keep_log(gas,amount, gas_type):
    price = gas_pump_core.gas_price(gas,amount)
    message = '\n{}, {}, ${}'.format(gas_type, amount, price)
    with open('log.txt', 'a') as file:
        file.write(message)

def in_the_log():
    left = []
    with open('log.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([split_string[0], float(split_string[1]), float(split_string[2].strip().replace('$', ''))])
    return left

def revenue_log():
    """return float value of total dollars spent"""
    left = in_the_log()
    price = 0
    with open('tank.txt', 'r') as file:
        for item in left:
            item[2] = float(item[2]) + float(item[2])
            price += item[2]
    return price
        
def in_the_tank():
    left = []
    with open('tank.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([split_string[0], float(split_string[1]), float(split_string[2])])
    return left

def take_away(gas_type, amount):
    str_l = ['type, amount_in_tank, price']
    left = in_the_tank()
    for item in left:
        if item[0] == gas_type:
            if float(amount) > float(item[1]):
                return False
            else:
                item[1] = float(item[1]) - float(amount)
        item[1] = str(item[1])
        item[2] = str(item[2])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)

    with open('tank.txt', 'w') as file: 
        file.write(message)
    return True

def refill():
    str_l = ['type, amount_in_tank, price']
    left = in_the_tank()
    for item in left:
        if item[1] < 5000.0:
            item[1] = 5000.0
        item[1]=str(item[1])
        item[2]= str(item[2])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)  

    with open('tank.txt', 'w') as file:
        file.write(message)
 
 
# def take_away(gas_type, amount):
#     str_l = ['type, amount_in_tank, price']
#     left = in_the_tank()
#     for item in left:
#         if item[0] == gas_type:
#             if float(amount) > float(item[1]):
#                 print("Sorry! We ran out of this type of gas!")
#                 return False
#             else:
#                 item[1] = float(item[1]) - float(amount)
#         item[1] = str(item[1])
#         item[2] = str(item[2])
#         str_l.append(', '.join(item))
#         message = '\n'.join(str_l)

#     with open('tank.txt', 'w') as file: 
#         file.write(message)
#     return True