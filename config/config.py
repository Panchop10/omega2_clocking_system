"""Configuration file for Clocking System"""

#Python Modules
from enum import Enum
from pathlib import Path

class Config(Enum):
    #CURRENT DIRECTORY
    PROJECT_DIR = str(Path().absolute())

    #USER SETTINGS
    DELAY_SECONDS = 10 #DELAY FOR CLOCKING AGAIN IN SECONDS (AVOID DUPLICATE)
    OLED_EXPANSION = 1 #1 = ON OR 0 = OFF (USE OLED EXPANSION)
    ID_STOP_SYSTEM = "b5c6e7bb" #Card id to stop the system

    #DONT CHANGE
    OK_IMG = PROJECT_DIR+"/img/image_ok.lcd" #Path for OK img
    ERROR_IMG = PROJECT_DIR+"/img/image_error.lcd" #Path for error img

    #MYSQL CONFIGURATION
    HOST = "192.168.1.233"
    PORT = "3307"
    USER = "omega"
    PASSWD = "0m3g4n3d*"
    DATABASE = "staff"

    #GOOGLE SPREADSHEET CONFIGURATION
    KEY_FILE = PROJECT_DIR+"/google_spreadsheet/omega_ned_key.json"
    SPREADSHEET_NAME = "timeclock_system"
