#!/usr/bin/env python3

import requests ## 3rd party URL lookup

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    
    startdate = "start_date =" + input ("Chose a start date (YYYY-MM-DD)")  ## start date from usr
    enddate = "&end_date=" + input ("Chose a end date (YYYY-MM-DD)") ## end date from user
    mykey = '&api_key=GUi3WOIHrksyfld4sz503GhgZlL0l9qymu4sMKTm' ## API key

    neourl = neourl + startdate + mykey

    neojson = (requests.get(neourl)).json()

    print(neojson)

## call main
main()

