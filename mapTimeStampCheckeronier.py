#!/usr/bin/python3
#Auth: Kube, James
#AuthDate: 20200705

#   ---------------------------------------------------------------------------
#  |Purpose:
#  |---------------------------------------------------------------------------
#  |Check Kubra outage map for last update time to ensure that the last 
#  |uploaded file was successfully consumed by Kubra and updated on the outage
#  |map page.
#   ---------------------------------------------------------------------------

#   --------------------------------------------------------------------------
#  |Note:                                                                     |
#  |--------------------------------------------------------------------------|
#  |Kubra.com currently consumes files, and updates the map, every 15 minutes.|
#   --------------------------------------------------------------------------


import functioneririzerFluxCapacitor as fc

#Base url for Kubra without customer or customer site details
kubra_base_url = 'https://kubra.io/stormcenter/api/v1/stormcenters/'
#UPDATE BELOW!!!
    #Kubra customer specific hash (appears to be unique per customer?)
kubra_cust_base = '88888888-4444-4444-4444-111111111111'
#Kubra customer site specific hash (probably...?  Assuming this is allow for m\
kubra_cust_site = '88888888-4444-4444-4444-222222222222'
    #Example URL break down:
#https://kubra.io/stormcenter/api/v1/stormcenters/88888888-4444-4444-4444-1111\
        #11111111/views/88888888-4444-4444-4444-222222222222/currentState?preview=false




if __name__ != '__main__':
    print("You sure you read the intro?")

else:
    #fetch the data
    myData = fc.getTheData(kubra_base_url,kubra_cust_base,kubra_cust_site)

    #Parse and get our timestamp for further analysis
    lastUpdated = fc.parseTheData(myData)

    #Check to see if we updated within our desired timeframe
    # '0' == false and not desired | '1' == true and good
    analysisParalysisTime = fc.timeStampComparison(lastUpdated)

    if analysisParalysisTime == 0:
        print('Not updated recently, better tell someone')
    else:
        print('Checked, looks good boss...or at least didn\'t get a zero\
 return value')

