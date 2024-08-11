import pytest
@pytest.fixture()
def setup():
    print("I will execute first")
    yield
    print("I will execute last")

@pytest.fixture()

def dataLoad():
    print("user profile has being created")
    return ["Vinay","Bakoria","vinaybakoriaacademy.com"]

@pytest.fixture(params=["chrome","Firefox","Edge"])
def crossbrowser(request):
    return request.param
