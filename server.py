import asyncio
import websockets

# coroutine to handle communication with connected client
async def handle_client(websocket, _path):
    # Create string to send to client
    message = 'HELLO'

    # Send string to the client
    await websocket.send(message)

# Creates a WebSocketServer instance which contains event loop to listen for client connections
# Upon accepting client connection, websockets automatically invokes 'handle_client' coroutine
start_server = websockets.serve(handle_client, "127.0.0.1", 8080)

# Add listener task to event loop
asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()
