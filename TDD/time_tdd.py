# written in python 3.*
#-*- coding: utf-8 -*-
import time
#from price_tracking import checkwhetherThereIsNewCoin

def TryToParse():
    print("called!")

def TimeTDD():
    #print time.strftime("%H")
    #minT = int(time.strftime("%M"))
    #secT = int(time.strftime("%S"))
    hourT = 22
    minT = 35
    secT = 15
    #print minT + " : " +  secT
    #sleep(1) # every sec
    #SendStatusRegularlly()

    #if E_MODE == 0: # TRACKING mode
    #if hourT > 6 and hourT < 18:
    if (minT >= 50 or minT < 3) or (minT >= 20 and minT < 33):
        if secT == 15 or secT == 45:
            TryToParse()

def checkwhetherThereIsNewCoin():
    LAST_LIST = ['Ncoin1', 'Ncoin2', 'Ncoin3', 'Ncoin4']
    CURR_LIST = ['Ncoin1', 'Ncoin4', 'Ncoin3']
    #print "checkwhetherThereIsNewCoin() -> len(LAST_LIST) : " + str(len(LAST_LIST))

    if len(LAST_LIST) == 0 or len(CURR_LIST) == 0:
        return "nothing"

    print("len(LAST_LIST) : " + str(len(LAST_LIST)))
    print("len(CURR_LIST) : " + str(len(CURR_LIST)))
    
    if(len(LAST_LIST) == len(CURR_LIST)):
        return "nothing"

    newCoinSet= set(LAST_LIST) - set(CURR_LIST)
    if len(list(newCoinSet)) == 1:
        return list(newCoinSet)[0]

def MatchingAlgorithmTDD():
    a= checkwhetherThereIsNewCoin()
    print(a)

MatchingAlgorithmTDD()