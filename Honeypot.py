'''imports''' 
#ip address, username, and password logging module 
import logging

#storing the logging information 
from logging.handlers import RotatingFileHandler

#import the sockets 
import socket 

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
    'credinfos.log', 
    maxBytes=2000, 
    backupCount=5) #set up logging to store in file
logcredhandle.setFormatter(logformat)

thecredlogger.addHandler(loghandle) #add logging settings to the logger

'''the shell'''


'''
emshell function 
param:
    chl - the channel (way to sending strings over SSH)
    cip - client ip 

purpose - fake shell for the attacker to use
'''
def emshell(chl, cip):
    chl.send(b'corporate-jumpbox2$') #create the shell prompt start 
    command = b""   #listening variable to listen to commands 
    while True:
        char = chl.recv(1) #listen for user input (char by char) 
        chl.send(char) #send that user input to the channel

        if not char: #non char input, then close channel 
            chl.close() 
        
        command += char #combine char vars into a command 

        #the command engine
        if char == b"\r":

            #exit command 
            if command.sttrip() == b'exit':
                resp = b"\n end session"
                chl.close 

            #print working dir 
            elif command.strip() == b'pwd':
                resp = b"\n" + b'\\usr\local' + b'\r\n'
            
            #who am i command 
            elif command.strip() == b'whoami':
                resp = b"\n" + b"corpbox1" + b'r\n' 
            
            #ls (list files in dir) command 
            elif command.strip() == b'ls':
                resp = b"\n" + b"jumpbox1.conf" + b"r\n"

            #cat command 
            elif command.strip() == b'cat jumpbox1.conf':
                resp = b"\n" + b"goto ynbro.com" + b"r\n"
            
            #all else, just echo what the user entered 
            else:
                resp = b"\n" + bytes(command.strip()) + b"\r\n"

        chl.send(resp) #send the response 
        chl.send(b'corporate-jumpbox2$') #get the default diaglog 
        command = b"" #listen for the next command 

