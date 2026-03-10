# DO NOT UPDATE CODE BELOW THIS LINE
import random as ran
import subprocess as sp
import logging as lg
from test import test_coeff

lg.basicConfig(level=lg.INFO)
log = lg.getLogger(__name__)

def test_and_plot(cf, root_s):
  flag = test_coeff()

def get_input(flag=True):
  max_, min_ = 10, -11
  elst = list(range(min_,  max_,2)) #even
  olst = list(range(min_+1,max_,2)) #odd
  brkn_per = ran.randint(0,101)

  def update_lst(flag):
    lst = ['f', 'f']
    lst[0] = ran.choice(olst) if flag else ran.choice(elst)
    lst[1] = ran.choice(olst) if flag else ran.choice(elst)
    return lst

  sub_lst = update_lst(brkn_per % 2 == 0)
  options = ['f','f','f']
  options[0] = 0 if brkn_per < 30 else 1
  options[1] = -(sum(sub_lst))
  options[2] = sub_lst[0] * sub_lst[1]

  lst = ['f','f', 'f']
  type = [int, float, str, bool]
  if not flag:
    for i,o in enumerate(options):
      t = ran.choice(type)
      lst[i] = t(o)      
  else:
    t = ran.choice(type)
    for i,o in enumerate(options):
      lst[i] = t(o)
      
  return tuple(lst)
