import pytest

from PYTESTDEMO2.BaseClass import Baseclass


@pytest.mark.usefixtures("setup1")
class Test1:
    def test_fixturedemo1(self):
        print("i will execute step1")
    def test_fixturedemo2(self):
        print("i will execute step1")
    def test_fixturedemo3(self):
        print("i will execute step1")
    def test_fixturedemo4(self):
        print("i will execute step1")
    def test_fixturedemo5(self):
        print("i will execute step1")
    def test_fixturedemo6(self):
        print("i will execute step1")
    def test_fixturedemo7(self):
        print("i will execute step1")
@pytest.mark.usefixtures("editprofile")
class Test2(Baseclass):
    def test_editprofile(self,editprofile):
        log = self.getlogger()
        log.info(editprofile)
        log.info(editprofile[2])

@pytest.mark.usefixtures("crossbrowser")
def test_crossbrowser(crossbrowser):
    print(crossbrowser)
