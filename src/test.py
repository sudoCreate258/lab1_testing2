from my_logger import log

def test_coeff(cf,rts):
  if rts:
    size = len(rts)
    a,b,c = cf
    if   size == 1 and (b**2 - (4*a*c)) == 0:
      log.error("discriminent should be 0 for single root")
    elif size == 2 and (b**2 - (4*a*c)) > 0:
      log.error("discriminent should be >0 for double root")
      return True
  return False
