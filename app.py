from flask import Flask, render_template
from flask_socketio import SocketIO,emit
import dataset



app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def hello():
    return open('html/index.html').read()

@socketio.on('message')
def messagereceived(data):
    print (data)
    emit('message',data,broadcast=True)
    db = dataset.connect('sqlite:///banco.db')
    table = db['chatweb']
    table.insert(data)



if __name__ == '__main__':
    socketio.run(app,'127.0.0.1',3000)
