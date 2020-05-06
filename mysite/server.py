import os
import socketio
from socketio import AsyncServer, Server
import logging
import eventlet.wsgi


from werkzeug.middleware.proxy_fix import ProxyFix


sio = Server(async_mode="eventlet",logger=True)

# So now we have an action list for the server at least - forget multiple sessions for now?
@sio.event
def connect(sid, environ):
    print("connection attempted")



app =         app = ProxyFix(socketio.WSGIApp(sio), x_for=1, x_proto=1)


        
        # default to 0.0.0.0
eventlet.wsgi.server(eventlet.listen(('', 8000)), app)