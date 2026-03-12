from util import get_input, test_and_plot
from my_logger import log

# TODO - (INPUT) receive variable input - step 1
#my_input = get_input()
#xc_input = get_input(False)
coef, outpt = (1,-5, 6), (2,3)
#coef, outpt = (1,-6, 5), (1,5)
#coef, outpt = (1,-2, 1), (1)


# TODO - (PROCESS) sanitize variable input - step 2


# TODO - (PROCESS) control the logic for an edge case - step 3


# TODO - (PROCESS) control the logic for a normal case - step 4


# TODO - (OUTPUT) standardize output using logger - step 5
log.info(outpt)

# TODO - (OUTPUT) test and plot graph - step 6
test_and_plot(coef, outpt)
