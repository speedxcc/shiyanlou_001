#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import sys
import csv

class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]

        if len(self.args) == 6
            index = self.args.index('-c')
            configfile = self.args[index + 1]
        
            index = self.args.index('-d')
            userfile = self.args[index + 1]

            index = self.args.index('-o')
            outputfile = self.args[index + 1]
        else:
            print("parameters Error")

    def configfile(self):
        return configfile
    def userfile(self):
        return userfile
    def outputfile(self):
        return outputfile

class Config(object):

    def __init__(self):
        self.config = self._read_config()
        
    def _read_config(self):
        config = {}
        with open(Args.configfile) as file:
            for line in file:
                prop = line.strip()
                name, rate = prop.split('=')
                config[name] = rate

#    def JishuL(self):
#       return config[JishuL]

#    def JishuH(self):
#        return config[JishuH]

#    def YangLao(self):
#        return config[YangLao]


     
class UserDate(object):
    
    def __init__(self):
        self.userdata = self._read_users_data()

    def _read_users_data(self):
        userdata = []

        with open(Arg.userfile) as file:
            for line in file:
                user = line.strip()
                person = tuple(user.split(','))
                userdata.append = person
    

def IncomeTaxCalculator(object):
    
    def calc_for_all_userdata(self):
        for person in userdata:
            number = person[0]
            gongzi = person[1]
                            
