# -*- coding: utf-8 -*-
"""
@author: Alex Testa
"""
import function as fun

uscita = "y"
while uscita == "y":
    url = str(input("\nGive me a url : "))
    element = fun.cleanString(fun.takeElementByTag(url, "html"))
    clean_element = fun.cleanStringChar(element)
    number_phone = fun.searchPhoneNumber(clean_element)
    email = fun.searchEmail(element)
    
    print("\n*****************")
    print("URL : \n" + url)
    print("*****************")
    
    print("\n*****************")
    print("EMAIL FOUND")
    print("*****************")
    for mail in email:
        print("Possible mail found : " + mail)


    print("\n*****************")
    print("PHONE FOUND")
    print("*****************")
    for number in number_phone:
        print("Possible number found : +" + number)
    
    print("*****************")
    uscita = str(input("\nVuoi cercare un'altro link? (y,n) : "))
    print("*****************\n")
