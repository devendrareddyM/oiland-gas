"""
File                :   config

Description         :

Author              :   LivNSense Team

Date Created        :   30-03-2020

Date Last modified :

Copyright (C) 2018 LivNSense Technologies - All Rights Reserved

"""
import logging
import logging.handlers as handlers

log_filename = 'vicas-health-monitoring'


###############################################################################
# LOGGING CONFIGURATION
log_dir_path = "logs"

# logger name will be given of the module name
logger = logging.getLogger(__name__)

"""
Help Regarding  Logging messages which are less severe than level will be 
ignored

Below is the order for the logging level

---------------------------
Level	    Numeric value
---------------------------
CRITICAL	50
ERROR	    40
WARNING	    30
INFO	    20
DEBUG	    10
NOTSET	    0
---------------------------
"""
# Here we define our Logging Level
logger.setLevel(logging.INFO)

# Here we define our formatter
formatter = logging.Formatter(
    '%(asctime)s.%(msecs)03d %(levelname)s %(filename)s %(module)s - %('
    'funcName)s:%(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# log file name and location declaration

file_name = '{}/{}.log'.format(log_dir_path, log_filename)


"""
Help Regarding setting the time rotating interval

------------------------------------------------------------------------------
Value	    Type of interval	If/how atTime is used
------------------------------------------------------------------------------
'S'	        Seconds	            Ignored
'M'	        Minutes	            Ignored
'H'	        Hours	            Ignored
'D'	        Days	            Ignored
'W0'-'W6'	Weekday (0=Monday)	Used to compute initial rollover time
'midnight'	Roll over at midnight, if atTime not specified, else at time atTime
Used to compute initial rollover time
-------------------------------------------------------------------------------
"""

logHandler = handlers.TimedRotatingFileHandler(file_name, when='midnight',
                                               interval=1, backupCount=30,
                                               encoding=None, delay=False,
                                               utc=False, atTime=None)

logHandler.setFormatter(formatter)

logger.addHandler(logHandler)
