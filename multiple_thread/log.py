#!/usr/bin/python
# -*- coding: UTF-8 -*-

###############################################################
#
#This script is used to output log to file
#Version : 1.0.0.1
#usage : 

import sys

#log to file
class Log:
    __output_file_obj = None
    
    def __init__(self):
        pass

    def __del__(self):
        if self.__output_file_obj:
            self.__output_file_obj.close()
    
    def set_log_path(self, log_path):
        self.__output_file_obj = open(log_path, "a+")
        
    def log(self, msg):
        if self.__output_file_obj:
            print >> self.__output_file_obj, msg
        print(msg)


log_obj = Log()
def set_log_path(log_path):
    log_obj.set_log_path(log_path)

def log(*tupleArg):
    msg = ""
    for item in tupleArg:
        msg += str(item) + " "
    msg = msg.rstrip()
    log_obj.log(msg)

############################# main ##################################
if __name__ == '__main__':
    log_obj.set_log_path("log.log")
    log("hello", 11)