from util import log

def test_coeff(cf,rts):
  if not rts:
    return False
  else:
    size = len(rts)
    a,b,c = cf
    if   size == 1 and (b**2 - (4*a*c)) == 0:
      log.info("discriminent should be 0 for single root")
    elif size == 2 and (b**2 - (4*a*c)) > 0:
      log.info("discriminent should be >0 for double root")
    else:            
      return False
