import psutil 
import sys
import os
import time

try :
	procroc = psutil.Process(int(sys.argv[1]))
except:
	print "NOT ENOUGH ARGUMENTS!"
else:
	print "process ID: ", proc.pid
	print "process Name: ", proc.name
	print "process Status: ", proc.status
	print "process Parent ID: ", proc.ppid
	print "process Parent Name: ", procsutil.Process(proc.ppid).name
	print "Process Creation Time:", time.ctime(proc.create_time)
	print "Files oprocened by the procrocess info:", proc.get_open_files()
	print "Memory Info (In Bytes):", proc.get_memory_info()


