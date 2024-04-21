import setu
import password
import hackchat

def message_got(chat, message, sender):
    if "hello" in message.lower():
        chat.send_message("Hello there {}!".format(sender))

chat = hackchat.HackChat("HelloBot", "programming")
chat.on_message += [message_got]
chat.run()