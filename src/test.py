from my_logger import log

def test_coeff(cf,rts):
  if rts:
    single_rt_flag = type(rts) == tuple and len(rts) == 1

    try:
      if single_rt_flag:
        r1,r2 = rts[0],0
      else:
        r1,r2 = rts[0], root_s[1]
    except Exception as e:
      err_log = f"{rts[0]} {rts[1]}, {cf} {type(rts)}, {e}"
      print(err_log)
      log.error(err_log)
      exit()
    try:
      a,b,c = cf
      a/0
    except Exception as e:
      err_log = f"{cf}, {e}"
      print(err_log)
      log.error(err_log)
      exit()
    
    if single_rt_flag and (b**2 - (4*a*c)) != 0:
      log.error(f"discriminent should be 0 for single root abc={cf},roots{rts}")
    elif not single_rt_flag and (b**2 - (4*a*c)) < 0:
      log.error(f"discriminent should be >0 for double root abc={cf},roots{rts}")
    else:
      return cf,True

  return cf, False
