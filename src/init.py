import setu
import password
import hackchat

def message_got(chat, message, sender):
    if ':!help' == message:
        chat.send_message("Command list:```help,afk,setu,back,time,lookup```")
    if ':!setu' == message:
        chat.send_message(setu.random_picture())
    if ':!afk' == message:
        chat.send_message("@{} You're AFK now.".format(sender))
    if ':!back' == message:
        chat.send_message("@{} Welcome back.".format(sender))

chat = hackchat.HackChat(password.username,"lounge")
chat.on_message += [message_got]
chat.run()