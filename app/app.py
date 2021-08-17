import asyncio
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def asynchronous():
    return 'The asynchronous API call has completed.'


@app.route("/test", methods=["GET"])
def synchronous():
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asynchronous_timer())
    return 'The synchronous API call has completed.'


async def asynchronous_timer():
    await asyncio.sleep(600)
    return 1

if __name__ == '__main__':
    app.run(host='0.0.0.0')
