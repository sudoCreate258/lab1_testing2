# DO NOT UPDATE CODE BELOW THIS LINE
import random as ran

def get_input(flag=True):
  max_, min_ = 20, -21
  elst = list(range(min_,  max_,2)) #even
  olst = list(range(min_+1,max_,2)) #odd
  brkn_per = ran.randint(0,101)

  options = [0               if brkn_per < 30     else 1, 
            ran.choice(olst) if brkn_per > 50     else ran.choice(elst),
            ran.choice(elst) if brkn_per % 2 == 0 else ran.choice(olst),]
  type = [int, float, str]
  lst = ['f','f','f']
  
  if not flag:
    for i,o in enumerate(options):
      t = ran.choice(type)
      lst[i] = t(o)      
  else:
    t = ran.choice(type)
    for i,o in enumerate(options):
      lst[i] = t(o)
      
  return tuple(lst)

def log_output():
  pass

def print_commits():
  pass

def test_and_plot():
  pass
