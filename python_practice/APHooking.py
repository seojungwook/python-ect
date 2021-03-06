import utils
import sys

from pydbg import * 
from pydbg.defines import *

'''
BOOL WINAPI WriteFile(
   _IN_        HANDLE hFile,
   _IN_        LPCVOID lpBuffer,
   _IN_        DWORD nNumberOfBytesToWrite,
   _OUT_opt_   LPDWORD lpNumberOfBytesWritten,
   _INPUT_OPT_ LPOVERLAPPED lpOverlapped
   );
'''

dbg = pydbg()
isProcess = False

orgPattern  = "love"
repPattern  = "hate"
processName = "notepad.exe"

def replaceString(dbg, args):
      buffer = dbg.read_process_memory(args[1], args[2])
      
      if orgParttern in buffer:
          print ("[APIHOOKING] Before : %s" %buffer)
          buffer  = buffer.replace(orgPattern, repPattern)
          replace = dbg.write_process_memory(args[1], buffer)
          print ("[APIHOOKING] After : %s" %dbg.read_process_memory(args[1],args[2]))
      return DBG_CONTINUE
      
for(pid, name) in dbg.enumerate_processes():
    if name.lower() == processName :
      
        isProcess = True
        hooks = utils.hook_container()
      
        dbg.attach(pid)
        print ("saves a process handle in self.h_process of pid[%d]" % pid)
      
        hookAddress = dbg.func_resolve_debuggee("kernel32.dll", "WriteFile")
      
        if hookAddress:
          hooks.add(dbg, hookAddress, 5, replaceString, None)
          print ("sets a bbreakpoint at the designated address : 0x%08x" % hookAddress)
          break
        else:
          print ("[Error]: couldn't resolve hook address")
          sys.exit(-1)
if isProcess:
    print ("waiting for occurring debugger event")
    dbg.run()
else:
    print ("[Error] : there is no process [%s]" % ProcessName)
    sys.exit(-1)
