# Failing test

def test_failing():
    assert (1, 2, 3) == (3, 2, 1)


# Ran 'pytest test_two.py -v'

# Results 

# ============= test session starts ==============================
# E         At index 0 diff: 1 != 3E         Full diff:
# E         - (3, 2, 1)
# E         ?  ^     ^
# E         + (1, 2, 3)
# E         ?  ^     ^
# 
# test_two.py:2: AssertionError
# =================================== short test summary info ==== 
# FAILED test_two.py::test_failing - assert (1, 2, 3) == (3, 2, 1)
# ====================================== 1 failed in 0.07s =======


# the extra section demonstrating where the test fails is called a traceback 
#  pytest adds little carets (^) to show us exactly what’s different