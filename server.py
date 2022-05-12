# Very Basic Echo Server

try:
    import asyncio
    from websockets import serve
except:
    import subprocess
    subprocess.call("pip install -r requirements.txt", shell=True)

    import asyncio
    from websockets import serve


connected = set()


async def echo(websocket, path):
    connected.add(websocket)

    try:
        async for message in websocket:
            for conn in connected:
                await conn.send(message)
            print("RECIEVED MESSAGE: " + message)
    finally:  # Cannot be Except, or the server is not going to work after a client disconnected
        connected.remove(websocket)


async def main():
    async with serve(echo, "", 6969):  # Hostname must be empty or it won't work
        await asyncio.Future()  # run forever

asyncio.run(main())
