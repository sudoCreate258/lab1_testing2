import pytest

def test_single_root(cf):
  _,b,c = cf
  assert (b**2 - (4*a*c)) == 0, "discriminent should be 0 for single root"

def test_double_root():
  _,b,c = cf
  assert (b**2 - (4*a*c)) > 0, "discriminent should be >0 for double root"

def test_coeff(cf,rts):
  if not rts:
    return False
  else:
    size = len(rts)
    if   size == 1:  test_single_root(cf)
    elif size == 2:  test_double_root(cf)
    else:            return False
    return True
