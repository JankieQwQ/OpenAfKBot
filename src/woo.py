import flask
import hackchat
import _thread

message_list = ''

def message_got(chat, message, sender):
    global message_list
    if len(message_list) > 20:
        message_list = []
    else:
        message_list += "{}: {}\n".format(sender,message)

webapp = flask.Flask(__name__)
webapp.config['JSON_AS_ASCII'] = False
webapp.json.ensure_ascii = Flase
@webapp.route('/')
def root():
    return {"code":200}

@webapp.route('/message')
def message():
    return str(message_list)

def webstart(obj):
    obj.run(port=2323,host='0.0.0.0')

def start():
    chat = hackchat.HackChat("woo","lounge")
    chat.on_message += [message_got]
    _thread.start_new_thread(webstart, (webapp,))
    chat.run()

start()