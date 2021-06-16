import asyncio
import time

async  def func():
    for _ in range(10):
        time.sleep(1)
        print(_)

# asyncio.run(func())
# print('started')

async  def main():
    await func()
    print('stopped')

print("started")
asyncio.run(main())
