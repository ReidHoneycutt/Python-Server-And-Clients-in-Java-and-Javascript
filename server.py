import asyncio
import websockets
import os
import time

async def send_random_data(websocket, path):
    # Wait for a few seconds
    await asyncio.sleep(3)  # Waits for 3 seconds

    # Generate a random byte string of length 10
    random_bytes = b'AAAAAA'

    # Send the random byte string to the client
    await websocket.send(random_bytes)

start_server = websockets.serve(send_random_data, "127.0.0.1", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
