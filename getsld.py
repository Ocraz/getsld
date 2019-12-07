#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re

aInFqdn = []

fileDoubleTld = "doubletld.txt"
fileSingleTld = "singletld.txt"


def removeTld(sFqdn, fileTld):
    #aFqdnCapped = []
    global aInFqdn
    
    f = open(fileTld, 'r')
    aTld = f.readlines()
    f.close()

    for sTld in aTld:
        sTld = sTld.strip()
        
        strTld.replace(".", "\.")
        if sFqdn.endswith(sTld):
            sFqdnCapped = re.sub(r'\.'+sTld+"$", '', sFqdn)
            aInFqdn.remove(sFqdn)
            
        #if sFqdn != sFqdnCapped:
            #aFqdnCapped.append(sFqdnCapped)
      #  if aInFqdn.count(sFqdn) > 0:
            #print ("removing " + line2 + " from " + sFqdn)
            #print ( aInFqdn.count(sFqdn))
            
       #     break
            print ( sFqdnCapped)
        #else:
         #   print ("not removing: " + ">"+sFqdn+"<" + ">"+sFqdnCapped+"<" + line2 + "<")
    #print (sFqdn)                
    #print (sFqdnCapped)                
    

for sInFqdn in sys.stdin:
    aInFqdn.append(sInFqdn.strip())

print ("Double TLDs stripped")
for sInFqdn in aInFqdn:
    sInFqdnCapped = removeTld(sInFqdn, fileDoubleTld)
    #sys.stdout.write (sInFqdnCapped+"\n")
    #for sStrippedFqdn in aInFqdn:
        #sys.stdout.write (sStrippedFqdn + "\n")

print ("")
print ("Single TLDs stripped")
for sInFqdn in aInFqdn:
    sInFqdnCapped = removeTld(sInFqdn, fileSingleTld)
    #sys.stdout.write (sInFqdnCapped+"\n")
    #for ssippedFqdn in aInFqdn:
     #   sys.stdout.write (ssippedFqdn + "\n")

sys.stdout.write ("\n")
    