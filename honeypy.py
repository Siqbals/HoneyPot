'''imports'''
#import library to parse command line arguments 
import argparse

#import our ssh 
from sshhoney import *

'''parse args'''

if __name__ == "__main__":
    parser = argparse.ArgumentParser() #create parse instance 

    #add the client ip argument, make it required 
    # *-a, --address) -> the ip address
    parser.add_argument('-a', '--address', type=str, required=True)

    #add the port argument
    parser.add_argument('-p', '--port', type=int, required=True)

    #add the username, not required
    parser.add_argument('-u', '--username', type=str)

    #add the password argument 
    parser.add_argument('-pw', '--password', type=str)

    #add the ssh argument, just store it as true, if not supplied then false
    parser.add_argument('-s','--ssh', action="store_true")

    #add the web based honeypot argument 
    parser.add_argument('-w', '--http', action="store_true")

    #combine all the argument to create argyment list 
    args = parser.parse_args()

    #decide which honeypot version to initiate 
    try:
        if args.ssh:   #ssh based honeypot
            print("try loop entered, running shh honeypot")
            honeypot(args.address, args.port, args.username, args.password)
        elif args.http:
            print("try loop entered, running HTTP honeypot")

            pass
        else:
            print("try looped entered, no specific honeypot selected (SSH or HTTP)")

    #exit case for if user wants to exit 
    except:
        print("exiting honeypy...")


            
    