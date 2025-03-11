import asyncio
from aioconsole import ainput



HOST = "127.0.0.1"
PORT = 8800


async def send_message(message, writer):
    writer.write(message.encode())
    await writer.drain()


async def listen_for_message(reader):
    while True:
        response = await reader.read(1024)
        if response:
            print(response.decode())
        else:
            break
        print("->: ", end="", flush=True)


async def listen_for_input(writer):
    while True:
        input_message = await ainput("->: ")
        if input_message:
            await send_message(input_message, writer)


async def main():
    try:
        reader, writer = await asyncio.open_connection(HOST, PORT)
        await asyncio.gather(listen_for_message(reader), listen_for_input(writer))
    except Exception as e:
        print(f"An error occurred in main() while handling messages: {e}")


if __name__ == "__main__":
    asyncio.run(main())
