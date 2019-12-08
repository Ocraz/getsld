#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import signal

def signal_handler(sig, frame):
        print("\nCtrl-C detected, exiting...\n")
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

aInFqdn = []

fileDoubleTld = "doubletld.txt"
fileSingleTld = "singletld.txt"

def removeTld(sFqdn, fileTld):
    
    f = open(fileTld, 'r')
    aTld = f.readlines()
    f.close()
    
    aFqdnToDotmp = []
    
    for sTld in aTld:
        sTld = sTld.strip()
                
        if sFqdn.endswith("." + sTld):
            sFqdnCapped = re.sub(r'\.' + sTld + "$", '', sFqdn)
            aFqdnToDotmp.append(sFqdn)
    return aFqdnToDotmp


for sInFqdn in sys.stdin:
    aInFqdn.append(sInFqdn.strip())

print ("Double TLDs stripped:")
aFqdnToDo = []
for sInFqdn in aInFqdn:
    aFqdnToDo = removeTld(sInFqdn, fileDoubleTld)

    #for sFqdnToDo in aFqdnToDo:
     #   aInFqdn.remove(sFqdnToDo)

    for sFqdnToDo in aFqdnToDo:
        print (sFqdnToDo)
    #aInFqdn.remove(sFqdnToDo)

        
#sys.exit()
print ("")
print ("Single TLDs stripped:")
for sInFqdn in aInFqdn:
    aFqdnToDo = removeTld(sInFqdn, fileSingleTld)
    for sFqdnToDo in aFqdnToDo:
        print (sFqdnToDo)
        #aInFqdn.remove(sFqdnToDo)

sys.stdout.write ("\n")
    