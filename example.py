#!/usr/bin/python
from pycodeinjection import *

PID = getPID("notepad.exe")
shellcode = generateShellcode("calc.exe")
injectShellcode(PID, shellcode)