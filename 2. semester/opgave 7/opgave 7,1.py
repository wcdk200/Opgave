import asyncio
import random

end_number = 20

async def producer(queue):
    while True: # Quits when randomly generated number equals end_number
        random_number = random.randint(1, 20)
        if random_number == end_number:
            print(f"Produced {random_number}, adding it, and quitting")
            await queue.put(random_number)
            await asyncio.sleep(random.uniform(0.1, 1.0))
            break
        else:
            print(f"Produced {random_number}, adding to queue.")
            await queue.put(random_number)
            await asyncio.sleep(random.uniform(0.1, 1.0))

async def printer(queue):
    while True:
        number = await queue.get()
        if number == end_number:
            break
        print(number)
        file = open('tekst7.txt', "w")
        file.write('Welcome to Geeks for Geeks')
        file.close()
        await asyncio.sleep(random.uniform(0.1, 1.0))


async def consumer(queue):
    while True: # Quits when randomly generated number equals end_number
        number = await queue.get()
        if number == end_number:
            print("Got the end number, quitting.")
            break
        print(f"Got number {number} from queue.")
        await asyncio.sleep(random.uniform(0.1, 1.0))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue()
    loop.run_until_complete(asyncio.gather(producer(queue),printer(queue), consumer(queue)))
    loop.stop()
    loop.close()