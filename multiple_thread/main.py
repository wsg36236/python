###############################################################
#
#This script is used to handle task by thread pool, but python multiple thread is not real using multiple cpu, just use for concurrent IO block tasks
#Version : 1.0.0.1
#usage : 
#
#
###############################################################

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os
import time
import threading
from thread_pool import ThreadPool
from log import log, set_log_path

def call_cmd(num, num2):
    log(threading.current_thread().getName(), ":", time.time(), num, num2)
    os.system('cmd /c "echo ' + str(num) + ' & pause"')


############################# main ##################################
if __name__ == '__main__':
    set_log_path("log.log")
    thread_pool = ThreadPool(call_cmd, 3)
    #thread_pool.start()
    for i in range(10):
        thread_pool.call(i, i)
    
    thread_pool.stop()
    log("")