# -*- coding: utf-8 -*-
"""
@author: Alex Testa
"""
import re
import requests
from bs4 import BeautifulSoup

#Chek if is valid email or not
def isEmail(email):
    #regular expression for validate email
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(pattern, email)):
        return True
    else:
        return False

def isNumberPhone(string):
    pattern = '[0-9]+'
    if re.findall(pattern, string):
        return True
    else:
        return False

#Chek if the url is valid
def isValidURL(url):
    if requests.get(url):
        return True
    else:
        return False

#Clean String of html tag
def cleanString(string):
    for element in string:
        return element.text.strip()

#Delete Space
def cleanStringChar(string):
    removeSpecialChars = string.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
    return removeSpecialChars.replace(" ","")

#Take element
def takeElementByTag(url, tag):
    if isValidURL(url) != True :
        print("Bad Request, ricontrolla l'url")
    else:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all(str(tag))
    return results

def searchPhoneNumber(string):
    numbers = []
    pattern = '[0-9]+'
    match = re.findall(pattern, string)
    if match:
        for number in match:
            if isNumberPhone(number) and len(number) >= 9 and len(number) <= 15:
                numbers.append(number)
    return numbers

def searchEmail(string):
    emails = []
    pattern = re.compile(r'\w+[@]\w+.\w+')
    match = re.findall(pattern, string)
    if match:
        for email in match:
            emails.append(email)
    return emails


