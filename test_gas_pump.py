import gas_pump_core

def test_gas_pump():
    assert gas_pump_core.get_gas_type('1') == 'Regular'

def test_gas_price():
    assert gas_pump_core.gas_price('one', '1') == 1.88

def test_gas_pump2():
    assert gas_pump_core.get_gas_type('2') == 'Midgrade'

def test_gas_price2():
    assert gas_pump_core.gas_price('two', '1') == 2.26

def test_gas_pump3():
    assert gas_pump_core.get_gas_type('3') == 'Premium'

def test_gas_price3():
    assert gas_pump_core.gas_price('three', '1') == 2.89