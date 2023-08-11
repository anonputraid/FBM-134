#!/usr/bin/python3
# -*- Author : Anonputraid -*-
#
#

import json as ini_db,os as system,sys,glob
from colorama import Fore, Back, Style
from lib.core import api_printout as opt
from random import choice


db = open("data/json/modules_metadata_base.json")
x = ini_db.load(db)


def metadata_base(init=True,n = 0):
    value = [
        "http-brute",
        "http-passwords",
        "http-version",
        "http-banner",
        "http-exit",
    ]

    Title = {
        "http-commond"
    }
    
    f = "http-characters"


    for a in Title:
        opt.printout(x[f]["c"] + x[a]["name"] + x[f]["b"])
        
    print(x[a]["description"])
    

    v = x[a]["Line"]

    if v == 7:
        opt.printout(x[f]["e"] + x[f]["a"])
        
    print(x[f]["d"]) 


    for b in value:
        if x[b]["key"] == False:
            opt.printout(x[b]["command"] + x[f]["a"])
        else:
            opt.printout(x[b]["command"] + x[f]["b"]) 

        print( x[b]["description"])
    
    print(x[f]["c"])


def clean(init="clear"):

    if system.name == "posix":
        command = [
            "http-clean"
        ]
        
        for a in command:
            b = x[a]["command"]
            if init == b:
                system.system(x[a]["command"])
    elif system.name == "nt":
        system.system("cls")

def version(init=True, n = 0):
    init_db = [
        "http-changelog",
    ]

    f = "http-characters"

    for a in init_db:
        opt.printout(x[f]["c"] + x[a]["version"] )
        
    print(x[a]["description"] + x[f]["c"])

def exit(init=True):
    if init == True:
        sys.exit(0)
    pass


def banner():
    """
    This Function Print FBM-134 Banner With its Version
    """

    absolute_path = glob.glob("data/logos/*.txt")

    for x in range(1):
        Logos_banner = choice(absolute_path)

        if system.path.isfile(Logos_banner):
            Logos = open(Logos_banner)
            print(Fore.RED + Logos.read() + Style.RESET_ALL)
            pass

def get_version():
    pass
