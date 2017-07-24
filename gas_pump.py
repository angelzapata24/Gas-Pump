import gas_pump_core
import disk


def main():
    
    print('\tHello! Welcome to AZ Gas.\n', end = '')
    msg = '''\n\tWhich type of gas would you like?\n
    \t1. Regular $1.88\n
    \t2. Midgrade $2.26\n
    \t3. Premium $2.89\n '''
    while True:
        gas = input(msg)
        if gas.lower() == 'refuel':
            disk.refill()
            print('Thanks refueled.')
            return None
        if gas.lower() == 'revenue':
            print('your total revenue is ${:.2f}'.format(disk.revenue_log()))
            return None 
        if gas == '1' or gas == '2' or gas == '3' or gas.lower() == 'one' or gas.lower() == 'two' or gas.lower() == 'three':
            break
        else:
            print('Sorry, invalid choice!')
    amount = input('How many gallons would you like? ')
    if not amount.strip().isnumeric():
        print("Sorry, invalid choice!")
        return None


    gas_type = gas_pump_core.get_gas_type(gas)
    if not disk.take_away(gas_type, amount):
        print("Come back again!")
        print("Sorry! We ran out of this type of gas!")
        return None

    print('Your total will be ${:.2f}'.format(gas_pump_core.gas_price(gas, amount)))
    gas_type = disk.keep_log(gas, amount, gas_type)
    print('Thank you for shopping with us today! Have a nice day!!')


if __name__ == '__main__':
    main()