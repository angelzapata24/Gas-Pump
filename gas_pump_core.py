
def gas_price(gas, amount):
    """ str -> Float"""
    if gas == '1' or gas.lower() == 'one':
        return float(amount) * 1.88
    elif gas == '2' or gas.lower() == 'two':
        return float(amount) * 2.26
    elif gas == '3' or gas.lower() == 'three':
        return float(amount) * 2.89

def get_gas_type(gas):
    """ (str, float) -> str"""
    if gas == '1' or gas.lower() == 'one':
         gas_type = 'Regular'
    elif gas == '2' or gas.lower() == 'two':
        gas_type = 'Midgrade'
    elif gas == '3' or gas.lower() == 'three':
        gas_type = 'Premium'
    return gas_type 

 
