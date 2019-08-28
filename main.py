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

#constantly scan for rfid tag presence
def __main__():
    """Open nfc reader continusly until a card is read"""

    #Image to check when main started
    oled_screen = Oled()
    oled_screen.msg_start()

    route = Routes()
    while True:
        print("before card reading")

        #Read card, the constructor will search for a card until it gets one
        card = Card()

        print("after card reading")

        #If debug options is active, show card id on screen
        if(Config.DEBUG.value):
            oled_screen.debug_msg(card.id)

        #break the loop if the card presented is the one configured to stop it
        if(card.id == Config.ID_STOP_SYSTEM.value):
           break

        route.register_timeclock(card.id)

if __name__ == '__main__':
    __main__()
