import os
import setu
import _thread
import password
import hackchat
import urllib.request

def message_got(chat, message, sender):
    if ':!help' == message:
        chat.send_message("Command list:```help,afk,setu,back,time,peep```")
    if ':!setu' == message:
        chat.send_message(setu.random_picture())
    if ':!afk' == message:
        chat.send_message("@{} You're AFK now.".format(sender))
    if ':!back' == message:
        chat.send_message("@{} Welcome back.".format(sender))
    if ':!peep' == message:
        try:
            message_list = urllib.request.urlopen('http://127.0.0.1:2323/message').read()
        except Exception as e:
            message_list = str(e)
        chat.send_message(message_list)
chat = hackchat.HackChat(password.username,"lounge")
chat.on_message += [message_got]
os.system('start cmd /c python woo.py')
chat.run()