import flask
import hackchat

message = []

def message_got(chat, message, sender):
    if len(message) > 20:
        message = []
    else:
        message.append("{}: {}".format(sender,message))
def start():
    chat = hackchat.HackChat("woo","lounge")
    chat.on_message += [message_got]
    chat.run()