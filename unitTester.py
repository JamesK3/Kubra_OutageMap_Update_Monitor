#!/usr/bin/python3
#Auth: Kube, James
#AuthDate: 20200705

#   ---------------------------------------------------------------------------
#  |Purpose:
#  |---------------------------------------------------------------------------
#  |Collection of unit tests
#   ---------------------------------------------------------------------------

import functioneririzerFluxCapacitor as fc
import json
import time

#map url
kubra_base_url = 'https://kubra.io/stormcenter/api/v1/stormcenters/'
#UPDATE BELOW!!!
kubra_cust_base = '88888888-4444-4444-4444-111111111111'
kubra_cust_site = '88888888-4444-4444-4444-222222222222'
#Example URL break down:
#https://kubra.io/stormcenter/api/v1/stormcenters/88888888-4444-4444-4444-1111\
#11111111/views/88888888-4444-4444-4444-222222222222/currentState?preview=false

#Unit testing....
#fetch the data
myData = fc.getTheData(kubra_base_url,kubra_cust_base,kubra_cust_site)
assert 'updatedAt' in myData.keys(), "Missing updatedAt key in return"
print("Good dict")

#Make sure we're returning an epoch timestamp
myEpochTimeStamp = fc.parseTheData(myDict)
assert myEpochTimeStamp > 0, "myEpochTimeStamp should be an epoch value not 0"
print("Good epoch")

#Check our epoch checker
analysisParalysisTime = fc.timeStampComparison(myEpochTimeStamp)
assert analysisParalysisTime == 1, "analysisParalysis should be 1 if good"
print("Good epoch compare")


