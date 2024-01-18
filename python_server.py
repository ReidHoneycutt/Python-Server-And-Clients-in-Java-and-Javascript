import asyncio
import websockets
import os
import time

async def send_random_data(websocket, path):
    # wait for 3 seconds
    await asyncio.sleep(3)
    random_bytes = b'AAAA'
    await websocket.send(random_bytes)
start_server = websockets.serve(send_random_data, "127.0.0.1", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
