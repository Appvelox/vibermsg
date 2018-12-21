from flask import Flask, request
from vibermsg import ViberClient, messages

app = Flask(__name__)
client = ViberClient('<YOUR_TOKEN>')


@client.register_text_message_processor()
def text_handler(incoming):
    msg = messages.TextMessage(incoming.message.text)
    client.send_message(incoming.sender.id, msg)


@app.route('/incoming')
def incoming():
    if request.json:
        client.process_json(request.json)
    return ''
