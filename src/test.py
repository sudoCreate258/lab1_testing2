from my_logger import log

def test_coeff(cf,rts):
  if rts:
    size = 1 if type(rts) == tuple else 2
    a,b,c = cf
    if   size == 1 and (b**2 - (4*a*c)) == 0:
      log.error(f"discriminent should be 0 for single root abc={cf},roots{rts}")
    elif size == 2 and (b**2 - (4*a*c)) > 0:
      log.error(f"discriminent should be >0 for double root abc={cf},roots{rts}")
    return True
  return False
