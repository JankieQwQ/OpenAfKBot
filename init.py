import os
import _thread

def startBot():
    os.system('start src/woo.py')
    os.system('start src/main.py')

_thread.start_new_thread(startBot,())