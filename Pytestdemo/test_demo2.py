# Any pytest file should start with test_ or ends with _test
# pytest method name should always starts with
# Any code should be wrapped under method
import pytest


# Running test cases from terminal
# cd -- path of the package -- py.test-- -v -- -s



# def test_thirdprogram():
#     msg = "Hello"
#     assert msg == "Hi" , "Test Failed because string not matched"


# if u want to run specific file:

# def test_thirdprogram():
#     msg = "Hello"
#     assert msg == "Hi" , "Test Failed because string not matched"
#
# def test_fourthprogram():
#     a = 10
#     b = 20
#     assert a + 10 == 20," addition donot match"

# py.test test_demo2.py -v -s

# def test_thirdprogram():
#     msg = "Hello"
#     assert msg == "Hi" , "Test Failed because string not matched"
#
# def test_fourthprogramCredit_Card():
#     a = 10
#     b = 20
#     assert a + 10 == 20," addition donot match"

# Command: py.test -k Credit_Card -v -s
# @pytest.mark.smoke
#
def test_initialtest1(setup):
    print("This is from second initial test case")