import pytest

@pytest.mark.xfail
def test_thirdprogram():
    msg = "hello"
    assert msg == "hi", "Failed string not matched"
@pytest.mark.smoke
def test_Credit():
    a = 10
    b= 20
    assert a + 10 == 20
