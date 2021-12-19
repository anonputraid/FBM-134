#!/usr/bin/python3
# -*- Author : Anonputraid -*-    
#
# Create a Wordlist About Target's Personal Data Automatically
# -*- Name : Createword. -*-
#

# Date: 13-06-2021


from lib.core import api_printout as opt
from colorama import Fore as init_a, Back, Style

import json as ini_db

db = open("data/json/modules_metadata_base.json")
x = ini_db.load(db)


def HacktivityActionJSON():
    value = [
        "http-generate"
    ]
    
    f = "http-characters"
    
    print(x[f]["c"])

    for a in value:
        opt.printout(x[a]["name"])

    print("")

    opt.printout(x[f]["e"])
    print("")
    pass



import os as system

def interactive():
    db = {}

    HacktivityActionJSON()
    
    db["db_main"] = input(init_a.YELLOW + "FirtsName: " + Style.RESET_ALL).lower()
    db["db_data"] = input(init_a.YELLOW + "Birthday:  " + Style.RESET_ALL) 
    db["db_user"] = input(init_a.YELLOW + "Nick Name: " + Style.RESET_ALL).lower()
    db["db_host"] = input(init_a.YELLOW + "Location:  " + Style.RESET_ALL).lower()
    
    interfuse(db)
    pass



import time 

def absolute_path(seq, start, init=""):
    for a in seq:
        for b in start:
            yield a + init + b


def other_values(name_db, init_db, path="wordlists"):
    init_db.sort()

    try:
        output = open("{}/{}".format(path,name_db),"w") 
        output.write(system.linesep.join(init_db))
        output.close()
    
        main_controller.adjective(name_db,path="wordlists")
    except KeyboardInterrupt:
        pass
    pass

import sys  

class main_controller():
    def adjective(name_db, path):
        init_db = open("{}/{}".format(path,name_db),"r")
        no = 0 
        for a in init_db:
            no += 1
        print(init_a.YELLOW
            + "Directori:\033[1;31m {}/{} ".format(path,name_db)
            + init_a.YELLOW 
            + "Counting \033[1;31m {} words.\033[1;m\n".format(str(no))
            )
        init_db.close()

        intr = input(init_a.BLUE + "Hyperspeed Print? (Y/n) : ").lower()
        
        if intr == "y":
            
            BannerWordlistsJSON()

            try:
                with open("{}/{}".format(path,name_db), "r+") as f:
                    a = f.readlines()
                    no = 0
                    for line in a:
                        no += 1 
                        sys.stdout.write("\033[1;33m" + line + Style.RESET_ALL)
                        sys.stdout.flush()
                        time.sleep(0000.1)
                    print("\n")

            except Exception as e:
                print("[ERROR]: " + str(e))
            pass
        pass
    pass

def BannerWordlistsJSON():
    value = [
        "http-wordlists"
    ]

    f = "http-characters"

    print(x[f]["c"])

    for a in value:
        opt.printout(x[a]["name"])
    print("")

    opt.printout(x[f]["e"])
    print("")
    pass

def interfuse(init_db):

    birthdate_a1 = init_db["db_data"][:2]
    birthdate_a2 = init_db["db_data"][2:4]
    birthdate_a3 = init_db["db_data"][-2:]
    birthdate_a4 = init_db["db_data"][-4:]
    
    db_a1 = [
        birthdate_a1,
        birthdate_a2
    ]

    db_a2 = [
        birthdate_a3,
        birthdate_a4
    ]

    birthdate_db1 = []
    birthdate_db2 = []

    for a in db_a1:
        birthdate_db1.append(a)
        for b in db_a1:
            if db_a1.index(a) != db_a1.index(b):
                birthdate_db1.append(a + b)
                birthdate_db2.append(a + b)


    birthdate_db3 = []

    for a in db_a2:
        birthdate_db3.append(a)
        for b in birthdate_db2:
            if db_a2.index(a) != birthdate_db2.index(b):
                birthdate_db3.append(b + a)


    db_b1 = init_db["db_main"].split(" ")

    name_db1 = []

    for a in db_b1:
        name_db1.append(a)
        for b in db_b1:
            if db_b1.index(a) != db_b1.index(b):
                name_db1.append(a + b)
                for c in db_b1:
                    if (
                        db_b1.index(a) != db_b1.index(b)
                        and db_b1.index(a) != db_b1.index(c)
                        and db_b1.index(b) != db_b1.index(c)
                    ):
                        name_db1.append(a + b + c)
                        for d in db_b1:
                            if (
                                db_b1.index(a) != db_b1.index(b)
                                and db_b1.index(a) != db_b1.index(c)
                                and db_b1.index(b) != db_b1.index(c)
                                and db_b1.index(a) != db_b1.index(d)
                                and db_b1.index(b) != db_b1.index(d)
                                and db_b1.index(c) != db_b1.index(d)
                            ):
                                name_db1.append(a + b + c)
    
    user_db2 = [
        init_db["db_user"]
    ]

    name_db2 = []

    for a in user_db2:
        name_db2.append(a)

    
    db_c1 = init_db["db_host"].split(",") 


    area_db1 = []

    for a in db_c1:
        area_db1.append(a)
        for b in db_c1:
            if db_c1.index(a) != db_c1.index(b):
                area_db1.append(a + b)
                for c in db_c1:
                    if (
                        db_c1.index(a) != db_c1.index(b)
                        and db_c1.index(a) != db_c1.index(c)
                        and db_c1.index(b) != db_c1.index(c)
                    ):
                        area_db1.append(a + b + c)
                        for d in db_c1:
                            if (
                                db_c1.index(a) != db_c1.index(b)
                                and db_c1.index(a) != db_c1.index(c)
                                and db_c1.index(b) != db_c1.index(c)
                                and db_c1.index(a) != db_c1.index(d)
                                and db_c1.index(b) != db_c1.index(d)
                                and db_c1.index(c) != db_c1.index(d)
                            ):
                                area_db1.append(a + b + c)


    api  = []
    api  = list(absolute_path(name_db1, birthdate_db1))
    api += list(absolute_path(name_db1, birthdate_db3))
    api += list(absolute_path(name_db2, birthdate_db1))
    api += list(absolute_path(name_db2, birthdate_db3))
    api += list(absolute_path(area_db1, birthdate_db1))
    api += list(absolute_path(area_db1, birthdate_db3))

    other_values(init_db["db_user"] + ".txt", api)
