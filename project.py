import asyncio
import socket
import sys
import random

HOST = "127.0.0.1"
PORT = 8800

client_writers = []
clients = []


async def handle_connections(reader, writer):

    addr = writer.get_extra_info("peername")

    if addr not in clients:
        print(f"New client connected: {addr}")
        client_writers.append(writer)
        clients.append(addr)

    try:
        while True:
            data = await reader.read(1024)
            if not data or data == "" or data == None:
                print(f"Client: {addr} disconnected")
                client_writers.remove(writer)
                writer.close()
                print(f"Closed connection from {addr}")
                await writer.wait_closed()
                break

            message = data.decode()
            print(f"Received: {message!r} from {addr}")
            print(f"Send: {message!r}")

            for c in client_writers:
                if c != writer:
                    c.write(data)
                    await c.drain()

    except Exception as e:
        print(
            f"failed to execute handle_connections: {e}")
        pass

# Our main function.
async def main():
    # enter try block so we can handle exceptions a.k.a errors.
    try:
        # chat_server 
        # handle_connections() is called whenever a new client connection is established.
        # handle_connections() receives a (reader, writer) pair as two arguments,
        # which are instances of the StreamReader() and StreamWriter() classes.
        chat_server = await asyncio.start_server(handle_connections, HOST, PORT)
    except Exception as e:
        print(f"Failed initialize chat_server in main(): {e}")
    addrs = ", ".join(str(sock.getsockname()) for sock in chat_server.sockets)
    print(f"Serving on {addrs}")

    async with chat_server:
        await chat_server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())