'''imports''' 
#ip address, username, and password logging module 
import logging

#storing the logging information 
from logging.handlers import RotatingFileHandler

'''consts'''
#constant to set logging format 
logformat = logging.Formatter('%(message)s')


'''log stuffs'''
thelogger = logging.getLogger('thelogger') #create instance of logging var
thelogger.setLevel(logging.INFO) #set logger to only show us INFO type information 

loghandle = RotatingFileHandler(
    'infos.log', 
    maxBytes=2000, 
    backupCount=5) #set up logging to store in file
loghandle.setFormatter(logformat)

thelogger.addHandler(loghandle) #add logging settings to the logger

'''shell command log '''
thecredlogger = logging.getLogger('thelogger') #create instance of logging var
thecredlogger.setLevel(logging.INFO) #set logger to only show us INFO type information 

logcredhandle = RotatingFileHandler(
    'infos.log', 
    maxBytes=2000, 
    backupCount=5) #set up logging to store in file
logcredhandle.setFormatter(logformat)

thecredlogger.addHandler(loghandle) #add logging settings to the logger
