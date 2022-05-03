# Simple Echo Server

# TODO:
# - add Broadcast functionality

import asyncio
from websockets import serve


async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)
        print(message)


async def main():
    async with serve(echo, "", 8080):
        await asyncio.Future()  # run forever

asyncio.run(main())
