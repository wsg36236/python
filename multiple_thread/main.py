﻿###############################################################
#
#This script is used to 
#Version : 1.0.0.1
#usage : 
#
#
###############################################################

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os
import threading
import Queue
from log import log, set_log_path

def call_cmd(num, num2):
    log(threading.current_thread().getName(), ":", num, num2)
    os.system('cmd /c "echo ' + str(num) + '"')


def thread_func(func, task_queue, stop_event):
    thread_name = threading.current_thread().getName()
    log("[info] start thread :", thread_name)
    while True:
        #must handle the task, than exit, otherwise, the last task may be not handle before thread exit
        try:
            func(*task_queue.get(timeout = 1))
        except Queue.Empty:
            if stop_event.is_set():
                break
    log("[info] end thread :", thread_name)

class ThreadPool(object):
    def __init__(self, func, thread_num = 5):
        self.__thread_num = thread_num
        self.__func = func
        self.__queue = Queue.Queue()
        self.__stop_event = threading.Event()
        self.__threads = []

    def start(self):
        for i in range(self.__thread_num):
            thread = threading.Thread(target = thread_func, args = (call_cmd, self.__queue, self.__stop_event))
            self.__threads.append(thread)
            thread.start()
    
    def stop(self):
        """if all done, must call this wait all tasks is handled"""
        log("[info] Wait thread exit...")
        self.__stop_event.set()        
        for i in range(self.__thread_num):
            self.__threads[i].join()
        log("[info] All thread is exit in ThreadPool.")

    def call(self, *tupleArg):
        if not self.__threads:
            self.start()
        
        #no wait a thread to handle
        self.__queue.put_nowait(tupleArg)

############################# main ##################################
if __name__ == '__main__':
    set_log_path("log.log")
    thread_pool = ThreadPool(call_cmd, 3)
    #thread_pool.start()
    for i in range(10):
        thread_pool.call(i, i)
    
    thread_pool.stop()
    log("")