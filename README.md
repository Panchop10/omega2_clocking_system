# Omega2 clocking system

## What is this ? <a name="introduction"></a>

- Clocking system is a simple Python project intended to keep a check-in time and check-out time of employees in a school. 
- While creating the project, we use Omega2 + device with  RFID and NFC expansion. 
- We consult with Onion Omega2 documentation.

See   https://docs.onion.io/omega2-docs/

- This is in development.


# Table of contents
1. [What is this ?](#introduction)
2. [Requirements](#requirements)
3. [How to use this ?](#paragraph2)
    1. [Quick Start](#subparagraph1)
    2. [User Setting](#subparagraph2)
    3. [MYSQL Configuration](#subparagraph5)
    4. [Working With RFID & NFC Expansion](#subparagraph3)
       1. [Installation](#subsubparagraph1)
       2. [Scanning RFID/NFC Tags](#subsubparagraph2)
       3. [Using Mifare Ultralight Cards](#subsubparagraph3)
    5. [Working With Google Spreadsheet and PYTHON](#subparagraph4)  
       1. [Google Drive API and Service Accounts](#subsubparag1)
4. [Testing](#testing)
5. [Built With](#build)
6. [License](#license)




## Requirements <a name="requirements"></a>

You need Python 3 to run clocking system. 

To install Python3, start by updating your package manager:

` opkg update` 

the full version of python3:

`opkg install python3`

See https://docs.onion.io/omega2-docs/installing-and-using-python.html

You'll need to connect mysql.

'pip3 install mysql -connector'


## How to use this ? <a name="paragraph2"></a>



### Quick Start <a name="subparagraph1"></a>


Get your Omega2 + up and running by following the [Omega2 + getting started guide](https://docs.onion.io/omega2-docs/first-time-setup.html).


The official Python package manager, pip, is the standard way of installing Python modules on a system.

We’ll need to first install pip on the Omega:


`opkg update`

`opkg install python-pip`


`opkg install nfc-exp`



### User Setting <a name="subparagraph2"></a>

To stop the system , you'll first need to read the card :

`ID_STOP_SYSTEM = "b5c6e7bb"` *-Card id to stop the system*

To avoid the duplicate , you'll need to use delay :

`DELAY_SECONDS = 30`*- Delay for clocking again in seconds*

To use Oled expansion , It should be 1 (ON) :

`OLED_EXPANSION = 1`*- 1 = ON or 0 = OFF*



### MYSQL Configuration <a name="subparagraph5"></a>



  `HOST = "192.168.1.233"`
  
  `PORT = "3307"`
  
  `USER = "omega"`
  
  `PASSWD = "0m3g4n3d*"`
  
  `DATABASE = "staff"`




### Working With RFID & NFC Expansion <a name="subparagraph3"></a>


The NFC & RFID Expansion brings contact-less RFID and NFC communication to the Omega ecosystem. 

See  https://docs.onion.io/omega2-docs/using-rfid-nfc-expansion.html


#### Installation <a name="subsubparagraph1"></a>


To use your RFID & NFC Expansion, you’ll first need to initialize the device:

` opkg update`

` opkg install nfc-exp`


#### Scanning RFID/NFC Tags <a name="subsubparagraph2"></a>

To scan an RFID/NFC Tag, you can use the `nfc-list` utility.


#### Using Mifare Ultralight Cards <a name="subsubparagraph3"></a>


`nfc-mfultralight` program is used to configure the ` Mifare Ultralight `type cards. You can read from the tag and write to it.


In order to scan the tag and store it to a file, please run the following command:

` nfc-mfultralight r mycardUltra.mfd`


To view the content of the file, use xxd utility by using the following command:

`xxd mycardUltra.mfd`

### Working With Google Spreadsheets and PYTHON <a name="subparagraph4"></a>

Use the spreadsheets to record the check-in , check-out times and total working hours for all employees.



#### Google Drive API and Service Accounts <a name="subsubparag1"></a>

To programmatically access your spreadsheet , You'll need to create a service account and OAuth2 credentials from the [Google API Console ](https://console.developers.google.com/)

1. Go to the Google APIs Console.

2. Create a new project.

3. Click Enable API. Search for and enable the Google Drive API.

4. Create credentials for a Web Server to access Application Data.

5. Name the service account and grant it a Project Role of Editor.

6. Download the JSON file.

7. Copy the JSON file to your code directory and rename it to google_spreadsheet/omega_ned_key.json

8.Find the timeclock_system-email inside google_spreadsheet/omega_ned_key.json. Back in your spreadsheet, click the Share button in the top right, and paste the timeclock_system email into the People field to give it edit rights. Hit Send.


See the [google_spreadsheet](https://github.com/Panchop10/omega2_clocking_system/tree/gspreadsheet/google_spreadsheet)for details 



See the [Accessing Google Spreadsheet Data using Python](https://towardsdatascience.com/accessing-google-spreadsheet-data-using-python-90a5bc214fd2)




## Testing <a name="testing"></a>

The basic ways to run tests:

1.Switch to Onion Omega2 screen in the terminal.

2.Configure file `config.py`

3.Run the `menu.py` ,set a department and create employees

4.Run the `main.py`

5.Read the card to RFID expansion



See [Running and Writing Tests](https://devguide.python.org/runtests/) for more on running tests.


## Build With  <a name="build"></a>

- [Atom](https://atom.io) *- Used to edit the code*
- [The MariaDB Foundation](https://mariadb.org) *- Used to generate the database*


## License  <a name="license"></a>

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/Panchop10/omega2_clocking_system/blob/test/LICENSE) file for details

