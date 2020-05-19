from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# backend for the public chat app, using flask

app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

@app.route( '/' )
#renders the template associated with the functions upon running chatup.py
def hello():
  return render_template( './chat.html' )

#print message to the console for the public chat app
def messageRecived():
  print( 'message was received!!!' )

#required socket to be connected
@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )

if __name__ == '__main__':
  socketio.run( app, debug = True )