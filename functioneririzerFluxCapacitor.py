#!/usr/bin/python3
#Auth: Kube, James
#AuthDate: 20200705

#   --------------------------------------------------------------------------
#  |Purpose:                                                                  |
#  |--------------------------------------------------------------------------|
#  |Check Kubra outage map for last update time to ensure that the last       | 
#  |uploaded file was successfully consumed by Kubra and updated on the       | 
#  |outage map page.                                                          |
#   --------------------------------------------------------------------------

#   --------------------------------------------------------------------------
#  |Note:                                                                     |
#  |--------------------------------------------------------------------------|
#  |Kubra.com currently consumes files, and updates the map, every 15 minutes.|
#   -------------------------------------------------------------------------- 

import json
import requests
import time

if __name__ == '__main__':
    print("...for the modules")

def getTheData(kubra_base_url,kubra_cust_base,kubra_cust_site):
    """
    Construct target URL and return the JSON
    """
    myURL = kubra_base_url+kubra_cust_base+'/views/'+kubra_cust_site+\
            '/currentState?preview=false' 

    myRequest = requests.get(myURL)
    myReturnDict = json.loads(myRequest.text)

    return myReturnDict

def parseTheData(kubra_output_data_json2Dict):
    """
    Parse the provided dict and return the epoch timestamp
    """
    if 'updatedAt' in kubra_output_data_json2Dict.keys():
        return kubra_output_data_json2Dict['updatedAt']
    else:
        return 0


def timeStampComparison(lastUpdatedEpochTimeStamp,desiredInterval=30):
    """
    Consume the provided epoch timestamp and compare tor our desired update
    interval.  

    Use 30 minutes as the default desired update interval to account for lagl

    return 0 if unexpected 'last update' timestamp, 1 otherwise
    """
    currEpochTime = time.time()

    epochDelta = int(currEpochTime - lastUpdatedEpochTimeStamp)
    #epochDeltaMinutes = epochDelta/60
    epochDeltaMinutes = epochDelta

    if epochDeltaMinutes <= desiredInterval:

        print("Here's our currEpochTime ",currEpochTime)
        print("Here's our lastUpdatedEpochTimeStamp ",lastUpdatedEpochTimeStamp)
        print("Here's our epochDeltaMinutes ",epochDeltaMinutes)
        return 1
    else:
        return 0
