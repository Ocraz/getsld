#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re


def removeTld(strFqdn, fileTld):
    arrFqdnCapped =[]
    f = open(fileTld, 'r')
    arrTld = f.readlines()
    f.close()

    for line in arrTld:
        line2 = line.strip()
        strFqdn = strFqdn.strip()
        
        line2.replace(".", "\.")
        strFqdnCapped = re.sub(r'\.'+line2+"$", '', strFqdn)
        
        if strFqdn != strFqdnCapped:
            arrFqdnCapped.append(strFqdnCapped)
            print ("strFqdn: "+strFqdn.strip())
            print ("strFqdnCapped:" +strFqdnCapped.strip())
            print ("line2: " + line2)
            print ("==========================")
        '''
        else:
            print ("(F) strFqdn: "+strFqdn.strip())
            print ("(F) strFqdnCapped:" +strFqdnCapped.strip())
            print ("(F) line2: " + line2)
            print ("==========================")'''
                
    return arrFqdnCapped


#fileDoubleTld = "doubletld.txt"
fileDoubleTld = "l2.txt"
fileSingleTld = "singletld.txt"

#arrTest = removeTld("www.google.co.uk", fileDoubleTld)
#for strTest in arrTest:


#sys.exit(0)

#strInput = sys.stdin.readlines
   
arrInFqdn = []

for strInFqdn in sys.stdin:
    arrInFqdn.append(strInFqdn)
    
for strInFqdn in arrInFqdn:
    print (strInFqdn)


sys.exit(0)
    
    #arrStrippedFqdn = removeTld(strInFqdn, fileDoubleTld)
    #print (strInFqdn)
#    for strStrippedFqdn in arrStrippedFqdn:
 #       sys.stdout.write (strStrippedFqdn)

    #arrStrippedFqdn = removeTld(strInFqdn, fileSingleTld)
    #print (strInFqdn)
#    for strStrippedFqdn in arrStrippedFqdn:
#        sys.stdout.write (strStrippedFqdn)

sys.stdout.write ("\n")
