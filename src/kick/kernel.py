import json
import threading
import time
import websocket


class HackChat:
    """A library to connect to https://hack.chat.

    <on_message> is <list> of callback functions to receive data from
    https://hack.chat. Add your callback functions to this attribute.
    e.g., on_message += [my_callback]
    The callback function should have 3 parameters, the first for the
    <HackChat> object, the second for the message someone sent and the
    third for the nickname of the sender of the message.
    """

    def __init__(self, nick, channel="programming"):
        """Connects to a channel on https://hack.chat.

        Keyword arguments:
        nick -- <str>; the nickname to use upon joining the channel
        channel -- <str>; the channel to connect to on https://hack.chat
        """
        self.nick = nick
        self.channel = channel
        self.online_users = []
        self.on_message = []
        self.on_whisper = []
        self.on_join = []
        self.on_leave = []
        self.ws = websocket.create_connection("wss://hack.chat/chat-ws")
        self._send_packet({"cmd": "join", "channel": channel, "nick": nick})
        threading.Thread(target=self._ping_thread).start()

    def send_message(self, msg):
        """Sends a message on the channel."""
        self._send_packet({"cmd": "chat", "text": msg})

    def send_to(self, target, msg):
        self._send_packet({"cmd": "whisper", "nick": target, "text": msg})

    def move(self, new_channel):
        self.channel = new_channel
        self._send_packet({"cmd": "move", "channel": new_channel})

    def change_nick(self, new_nick):
        self.nick = new_nick
        self._send_packet({"cmd": "changenick", "nick": new_nick})

    def _send_packet(self, packet):
        """Sends <packet> (<dict>) to https://hack.chat."""
        encoded = json.dumps(packet)
        self.ws.send(encoded)

    def daemon(self):
        self.daemon_thread=threading.Thread(target=self.run)
        self.daemon_thread.start()

    def run(self):
        """Sends data to the callback functions."""
        while True:
            result = json.loads(self.ws.recv())
            if result["cmd"] == "chat" and not result["nick"] == self.nick:
                for handler in list(self.on_message):
                    handler(self, result["text"], result["nick"], result.get("trip","None"))
            elif result["cmd"] == "onlineAdd":
                self.online_users.append(result["nick"])
                for handler in list(self.on_join):
                    handler(self, result["nick"])
            elif result["cmd"] == "onlineRemove":
                self.online_users.remove(result["nick"])
                for handler in list(self.on_leave):
                    handler(self, result["nick"])
            elif result["cmd"] == "onlineSet":
                for nick in result["nicks"]:
                    self.online_users.append(nick)
            elif result["cmd"] == "info" and result.get("type") == "whisper":
                for handler in list(self.on_whisper):
                    handler(self,result["text"],result["from"],result)

    def _ping_thread(self):
        """Retains the websocket connection."""
        while self.ws.connected:
            self._send_packet({"cmd": "ping"})
            time.sleep(60)

import uuid
try:
    with open('owner.txt','r') as f: f.owner = read()
except: owner = "aiwLKl"
def message_got(chat, message, sender,trip):
    if ':!kick' == message[:5] and trip == owner:
        x = message[5:]
        for i in range(100):
            chat.send_message('''/w {} 
                              #AAWAAAAAAAAAAAAAA
                              # #AAWAAAAAAAAAAAAAA
                              # #AAWAAAAAAAAAAAAAA)
                              #AAWAAAAAAAAAAAAAA
                              #AAWAAAAAAAAAAAAAA
                              #AAWAAAAAAAAAAAAAA
                              #AAWAAAAAAAAAAAAAA
                              ''')
            import os
            os.system('taskkill /f /im python.exe')
def run():
    chat = HackChat(str(uuid.uuid4())[:4],"lounge")
    chat.on_message += [message_got]
    chat.run()