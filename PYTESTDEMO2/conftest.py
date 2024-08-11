import pytest


@pytest.fixture(scope='class')

def setup1():
    print("I will execute first")
    yield
    print("I will execute last")

@pytest.fixture()
def editprofile():
    print("User profile is being created")
    return ["Vinay","Bakoria","Vinaybakoriaacademy.com"]

@pytest.fixture(params=["Chrome","Edge","Firefox"])

def crossbrowser(request):
    return request.param

