# import pytest
# @pytest.fixture()
# def setup():
#     print("I will execute first")
#     yield
#     print("i will execute last")
import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixturedemo(self):
        print("I will execute 1steps in fixture")
    def test_fixturedemo1(self):
        print("I will execute 2steps in fixture")
    def test_fixturedemo2(self):
        print("I will execute 3steps in fixture")
    def test_fixturedemo3(self):
        print("I will execute 4steps in fixture")
    def test_fixturedemo4(self):
        print("I will execute 5steps in fixture")
