import pytest

@pytest.mark.skip(reason="regular function")
def fun():
  return 3

@pytest.mark.shared
def test_fun():
  assert fun() == 3
