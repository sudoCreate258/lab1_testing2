def test_coeff(cf,rts):
  if not rts:
    return False
  else:
    size = len(rts)
    a,b,c = cf
    if   size == 1:  assert (b**2 - (4*a*c)) == 0, "discriminent should be 0 for single root"
    elif size == 2:  assert (b**2 - (4*a*c)) > 0, "discriminent should be >0 for double root"
    else:            return False
