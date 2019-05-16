#!/usr/bin/python3
import requests

server = "http://docker.hackthebox.eu:50383/"

logfile = open("logfile.txt","w")


for i in range(1000):
        payload = {'password': "leonardo"}
        r = requests.post(server, data=payload)

        logfile.write(str(r.status_code))
        logfile.write(r.text)

logfile.close()
