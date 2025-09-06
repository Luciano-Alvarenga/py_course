from Desafio_075_soma import soma

def test_soma_inteiros():
    assert soma(2, 3) == 5

def test_soma_decimais():
    assert soma(2.5, 3.1) == 5.6

def test_soma_negativos():
    assert soma(-2, -3) == -5