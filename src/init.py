import os
import setu
import _thread
import password
import hackchat
import urllib.request

readme = '''
Command list:
> help, afk, awa, back, time, peep, ping

Open source in [GitHub](https://github.com/JankieQwQ/OpenAfKBot)
'''

def message_got(chat, message, sender):
    if ':!help' == message:
        chat.send_message("")
    if ':!setu' == message:
        chat.send_message(setu.random_picture())
    if ':!afk' == message:
        chat.send_message("@{} You're AFK now.".format(sender))
    if ':!back' == message:
        chat.send_message("@{} Welcome back.".format(sender))
    if ':!awa' == message:
        try:
            message_list = str(urllib.request.urlopen('http://127.0.0.1:2323/message').read())
        except Exception as e:
            message_list = str(e)
        chat.send_message(message_list)
chat = hackchat.HackChat(password.username,"lounge")
chat.on_message += [message_got]
chat.run()