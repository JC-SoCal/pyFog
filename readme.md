# pyFog

pyFog is a simple API which uses mechanize to complete tasks through the [FOG Project](http://www.fogproject.org "FOG Project") web interface. There is example code in the example.py file. 

I wrote this API to easily automate a few tasks I need to commonly perform with FOG. If you do not see a function that you need to perform feel free to make a feature request or message me on twitter: [@JC_SoCal](http://twitter.com/JC_SoCal "@JC_SoCal")

## Requirments
* Python 2.7
* [Python Mechanize module](http://wwwsearch.sourceforge.net/mechanize "Mechanize")
* Python cookielib

## Functions

All functions return a tuple of a status and a message:  
**status** is a boolean.  

* *True* -- The function completed successfully.
* *False* -- There was a problem.

**message** is a string. The string will contain information relating to the status.

**pyFog.open(url)**:  
&nbsp;&nbsp;&nbsp;&nbsp;Opens a connection to the webpage. This is required prior to login.  
Arguments:  

* url -- string, website for fog, i.e.: http://localhost/fog/management/index.php  

**pyFog.login(username, password)**:  
&nbsp;&nbsp;&nbsp;&nbsp;Logs in to the fog web interface.  
Arguments: 

* username -- string, username used to login to fog  
* password -- string, password used to login to fog	  

**pyFog.logout()**:  
&nbsp;&nbsp;&nbsp;&nbsp; Logs out of the fog web interface.  
Arguments: 

* *None*

**pyFog.upload(hostname)**:  
&nbsp;&nbsp;&nbsp;&nbsp;Upload will pull an image from a client computer that will be saved on the server.  
Arguments:  

* hostname -- string, valid hostname from the host managment console 

**pyFog.deploy(hostname)**:  
&nbsp;&nbsp;&nbsp;&nbsp;Deploy action will send an image saved on the FOG server to the client computer with all included snapins.   
Arguments:  

* hostname -- string, valid hostname from the host managment console 

**pyFog.wol(hostname, schedule)**:  
&nbsp;&nbsp;&nbsp;&nbsp;Wake Up will attempt to send the Wake-On-LAN packet to the computer to turn the computer on. In switched environments, you typically need to configure your hardware to allow for this (iphelper).   
Arguments:  

* hostname -- string, valid hostname from the host managment console
* schedule -- string, optional. FORMAT: 'YYYY/MM/DD HH:MM' example: '2014/08/17 15:25' If not set the task will execute immediately. 
