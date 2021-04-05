#DOCUMENTATION
##Participant List Generator

###Intro: What is the Participant List Generator?
It creates Bigbluebutton participant lists based on the production.log files in greenlight.

First the programm reads the logfiles and caches the data in an array-list. Afterwards the array list will be 
processed to a dictionary. The dictionary has following keys, values:
key: "room_id" value: [logfiles][...][...]

Based on the dictionary all data will be processed to seperated room_id .csv files
Now we have login/logout lists of all rooms on our bigbluebutton server

__________________________________________________________________

UPDATE: 
- Readme: Added Troubleshooting - Added Install Guide 
- Codebase: Updated Error Handling to CLI out / updated directorys in files / 
__________________________________________________________________
1. Getting Started

Prerequisites - Step 1

1.1 Install Git (optional)
  
Windows (download installer):

- install git

- wirte in console: git --version

- if you don´t see something like this: git version 2.29...:

    

    download git installer:
    https://git-scm.com/download/win



Linux (Ubuntu 16.04+) (shell command installation):
  
- open console/shell

- wirte in your terminal: git --version

- if you don´t see something like this: git version 2.7.4:

- use following commands in your terminal:



    sudo apt-get update
    sudo apt-get install git-core

    
___________________________________________
1.2 Install Python (optional)
Windows (download installer):

- open cmd

- write in your terminal: python --version

- if you don´t see something like this: Python 3.9.1:

- install python3


    
    https://www.python.org/downloads/



Linux (Ubuntu 16.04+) (shell command installation):
  
- open console/shell 

- write in you terminal: python3 --version

- if you don´t see something like this: Python 3.9.1:

- use following commands in your terminal:



    apt-get update
    apt-get upgrade 
    apt-get install python3.9
    apt-get install python3.9-distutils

    
___________________________________________




Step 2

- install python pdf module with following command in your terminal:

Win:



    python3 -m pip install PyPDF2
    python3 -m pip install reportlab



Linux:



    python3 -m pip install PyPDF2
    python3 -m pip install reportlab

  

2 Install

2.1 Clone this repository to your BBB-Server


    https://github.com/VelimirMueller/bigbluebutton-logfile-generator.git 



2.2 Place your input Bigbluebutton logfile
(on your server greenlight/log/production.log) in the data/input/logfiles directory of this application

Attention: ! you need a custom greenlight instance running !
https://docs.bigbluebutton.org/greenlight/gl-customize.html

2.3 Setup the application

- modify file - go to directory: src/main.py and modfiy following line:

replace example.log with your file and path in main.py:

    
    class Main(...
    def __init__(...
        self.set...
        self.lp = LogfileProcessor("../data/input/logfiles/example.log", "r")


2.4 test the application

open terminal and type:

    
    cd "path of your logfile processor aplication"
    python3 main.py

-------------------------------------------------------------------
if you encounter any troubles - follow this guide:



Troubleshooting:
    

    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install python3.9
    sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.9 2
    sudo update-alternatives --config python
    sudo apt-get install python3.9-distutils

    ttributeError: module 'platform' has no attribute 'linux_distribution'        
    
    sudo apt remove python3-pip
    sudo python3.9 -m easy_install pip
    python -m pip install PyPDF2
    python -m pip install reportlab


__________________________________________________________________
__________________________________________________________________
