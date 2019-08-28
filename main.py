"""
Constantly scan looking for presence of a tag
If a tag is found the uid is compared with a database
and the data is sent to a google spreadsheet
"""

#User Modules
from card import Card
from config.config import Config
from routes import Routes
from omega_expansions.oled import Oled

# Python Modules
from datetime import datetime

#constantly scan for rfid tag presence
def __main__():
    """Open nfc reader continusly until a card is read"""

    #Image to check when main started
    oled_screen = Oled()
    oled_screen.msg_start()

    route = Routes()

    #System connected to the database and ready to work
    oled_screen.msg_ok("Ready", datetime.now())
    
    while True:
        #Read card, the constructor will search for a card until it gets one
        card = Card()

        #If debug options is active, show card id on screen
        if(Config.DEBUG.value):
            oled_screen.debug_msg(card.id)

        #break the loop if the card presented is the one configured to stop it
        if(card.id == Config.ID_STOP_SYSTEM.value):
           break

        route.register_timeclock(card.id)

if __name__ == '__main__':
    __main__()
