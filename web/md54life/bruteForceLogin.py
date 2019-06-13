#!/usr/bin/python3
import requests
import hashlib
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

server = "http://docker.hackthebox.eu:41172/"
error_string = "Too slow!"
logfile = open("logfile.txt","w")


for i in range(100):
    r = requests.get(server)
    parsed_html = BeautifulSoup(r.text)
    md5 = parsed_html.body.find('h3', attrs={'align':'center'}).text
    hash = hashlib.md5(md5.encode("utf8"))
    payload = {'hash': hash.hexdigest()}
    print(md5 + " " + payload["hash"])
    #r = requests.post(server, data=payload)

    logfile.write(str(r.status_code))

    #if(error_string not in r.text):
    logfile.write(r.text)
    #break;

logfile.close()
