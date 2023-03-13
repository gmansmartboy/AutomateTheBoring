# Exceptions are raised with a raise statement. In code, a raise 
# statement consists of the following:
#       raise Exception('This is the error message.')

# You can write the traceback information to a text file and
#  keep your program running.
import traceback
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')

# “I assert that the condition holds true, and if not, there 
# is a bug somewhere, so immediately stop the program.”
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
ages
# prints [15, 17, 22, 26, 47, 54, 57, 73, 80, 92]
assert ages[0] <= ages[-1] # Assert that the first age is <= the last age.

# However, let’s pretend we had a bug in our code.
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.reverse()
ages
# prints [73, 47, 80, 17, 15, 22, 54, 92, 57, 26]
assert ages[0] <= ages[-1] # Assert that the first age is <= the last age.

# Using the Assertation in a traffic light simulation.
# Stoplights facing north-south and east-west.
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

# You might think that switchLights() should simply switch
#  each light to the next color in the sequence. The code
#  might look like this.
def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green': 
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight == 'red': 
            stoplight = 'green'
# But if while writing switchLights() you had added an 
# assertion to check that at least one of the lights is 
# always red, you might have included the following at the 
# bottom of the function:
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
    
# Using the logging Module

# To enable the logging module to display log messages on 
# your screen as your program runs, copy the following to the 
# top of your program (but under the #! python shebang line):

import logging
logging.basicConfig(level = logging.DEBUG, format = ' %(asctime)s - $(levelname)s - %(message)s')

# Your logging message is passed as a string to these functions.
logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')

# Disabling Logging
# You simply pass logging.disable() a logging level, 
# and it will suppress all log messages at that 
# level or lower. So if you want to disable logging entirely, just add logging.disable(logging.CRITICAL) 
# to your program.
logging.disable(logging.DEBUG)
logging.disable(logging.INFO)
logging.disable(logging.WARNING)
logging.disable(logging.ERROR)
logging.disable(logging.CRITICAL)
logging.disable()

# Since logging.disable() will disable all messages
# after it, you will probably want to add it near 
# the import logging line of code in your program.

# Logging to a file
# The logging.basicConfig() function takes a filename keyword argument
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
