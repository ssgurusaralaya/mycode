#!/usr/bin/python3
"""Alta3 || Tracking ISS"""
import requests
MAJORTOM = 'http://api.open-notify.org/astros.json'
def main():
    helmetson= requests.get(MAJORTOM).json()
    print(helmetson)
main()
