# DO NOT UPDATE CODE BELOW THIS LINE
import random as ran
import subprocess as sp
import math
import matplotlib.pyplot as plt
import sympy as sp
from my_logger import log
from test import test_coeff

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

def test_and_plot(cf, root_s):
  flag = test_coeff(cf,root_s)
  if flag:
    r1,r2 = root_s
    a,b,c = cf

    mid = -b / (2 * a)
    offset = 12 if abs(r1 - r2) > 1.5 else 12
    x_vals = [i/10 for i in range(int((mid-10)*10), int((mid+10)*10))]
    y_vals = [a*(xi**2) + b*xi + c for xi in x_vals]
    
    plt.plot(x_vals, y_vals)
    plt.scatter([r1, r2], [0, 0], s=120, color='red', edgecolors='black', zorder=5)
    plt.annotate(f"({r1:.1f}, 0)", (r1, 0), textcoords="offset points", xytext=(0, offset), ha='center')
    plt.annotate(f"({r2:.1f}, 0)", (r2, 0), textcoords="offset points", xytext=(0, -18 if abs(r1-r2) < 1.5 else offset), ha='center')

    x_sym = sp.symbols('x')
    latex_equation = sp.latex(a*x_sym**2 + b*x_sym + c)
    
    plt.title(f"$f(x) = {latex_equation}$")
    plt.axhline(0, color='black', linewidth=1)
    plt.grid(True)
    plt.show()
    fname = f"graphs/lab1_test2_{"-".join(str(root_s))}.png"
    plt.savefig(fname, dpi=300)
    plt.close()

    log.info(f"graph complete see {fname}")
  else:
    log.warn(f"cannot graph {cf} produces {root_s}")

