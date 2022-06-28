from array import array
from flask import Flask, redirect, request
import os
from backend.Pod import Pod
from backend.Connection import Connection

import asyncio

env = os.environ.get("APP_ENV", "dev")
print(f"Starting application in {env} mode")

COUNT_OF_PODS = 5

def config_pods() -> array:
    return[ 
        Pod (f"http://localhost:4000{i}")
        for i in range(1,COUNT_OF_PODS)
    ]


async def fetch_html(url: str) -> str:
    resp = await request(method="GET", url=url)
    resp.raise_for_status()
    html = await resp.text()
    return html

async def handle_request(pod, connection) -> None:
    pod.create_connection()
    connection.set_pod_url(pod.url)
    html = await fetch_html(pod.url)
    if (html):
        connection.set_is_finalized()

    #TODO async function, wait to response +

class Balancier(Flask):
    _next = 0
    # pool of connections
    connections = [Connection] * 10000
    pods = config_pods()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def round_robin(self):
        for pod in self.pods:
            if pod.is_active:
                connection = Connection()
                try:
                    handle_request(pod, connection)
                except:
                    #TODO handle request fail
                    pass
                return redirect(pod.url)


app = Balancier(f"client")

# app.config.from_object(f"backend.{env}_settings")
app.server_id = 1

@app.route('/')
def hello_world():  # put application's code here
    return app.round_robin()

if __name__ == '__main__':
    app.run()
