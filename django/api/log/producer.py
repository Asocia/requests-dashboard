import asyncio

PERIOD = 0.5


async def readline(f):
    while True:
        data = f.readline()
        if data:
            return data
        await asyncio.sleep(PERIOD)


async def test():
    with open('api.log') as f:
        while True:
            line = await readline(f)
            print('Got: {!r}'.format(line))

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
