def test_ex1():
    assert 1 in [2, 3, 4]

def test_ex2():
    a = 27
    b = 3
    assert a < b 

def test_ex3():
    assert 'fizz' not in 'fizzbuzz'


# All tests failed
    # now let's pass them now  

def test_ex1p():
    assert 3 in [2, 3, 4]

def test_ex2p():
    a = 27
    b = 3
    assert a > b 

def test_ex3p():
    assert 'fizz' in 'fizzbuzz'