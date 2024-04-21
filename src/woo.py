import flask
import hackchat
import _thread

message = []

def message_got(chat, message, sender):
    if len(message) > 20:
        message = []
    else:
        message.append("{}: {}".format(sender,message))

webapp = flask.Flask(__name__)
@webapp.route('/')
def root():
    return {"code":200}

@webapp.route('/message')
def message():
    return str(message)

def webstart(obj):
    obj.run(port=2323,host='0.0.0.0')

def start():
    chat = hackchat.HackChat("woo","lounge")
    chat.on_message += [message_got]
    _thread.start_new_thread(webstart, ())
    chat.run()
