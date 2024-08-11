# Any pytest file should start with test_ or ends with _test
# pytest method name should always starts with
# Any code should be wrapped under method
# method name should have sense
# -k stands for method name execution, -s for logs in output, -v stands for more information like metadata
# u can run specific file with py.tset <Filename>
# u can mark(tag) tests @pytest.mark.smoke and then run it with -m
# u can skip test with @pytest.mark.skip
#@pytest.mark.xfail
#fixtures are used as setup and tear down methods for test cases - conftest file to generalize fixtures and make it
# available to all test cases
import pytest

##############################################################################################################################
# Running test cases from terminal
# cd -- path of the package -- py.test-- -v -- -s



# def test_firstprogram():
#     print("Hello")
#
# def test_secondprogram():
#     print("Good morning")

# def test_thirdprogram():
#     msg = "Hello"
#     assert msg == "Hi" , "Test Failed because string not matched"
#
# def test_fourthprogram():
#     a = 10
#     b = 20
#     assert a + 10 == 20," addition donot match"

# py.test test_demo2.py -v -s
##############################################################################################################################
# Run test case which have creditcard name


#
# def test_secondprogramCredit_Card():
#     print("Good morning")

# def test_fourthprogramCredit_Card():
#     a = 10
#     b = 20
#     assert a + 10 == 20," addition donot match"

# Command: py.test -k Credit_Card -v -s
##############################################################################################################################
# if u want to run test cases which are marked as smoke
# @pytest.mark.smoke
# def test_initialtest():
#     print("This is smoke related test case")

# py.test -m smoke -v -s
##############################################################################################################################

# U can skip the test case using @pytest.mark.skip
# @pytest.mark.smoke
# @pytest.mark.skip
# def test_initialtest():
#     print("This is smoke related test case")

##############################################################################################################################
# now if there is requirement like where u dont want to skip the test because this test case doing some operation
# which are like pre-reqisite
#for further test case

# @pytest.mark.xfail
# @pytest.mark.xfail
# def test_bug1(setup):
#     print("This is a bug which i don't want to show in my report")
##############################################################################################################################
# Fixtures:
# @pytest.fixture()
# def setup():
#     print("I will execute first")
# def test_fixturedemo(setup):
#     print('I will execute steps in fixtures')

def test_crossbrowser(crossbrowser):
    print(crossbrowser)