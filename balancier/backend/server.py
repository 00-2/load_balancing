from array import array
from flask import Flask, redirect
import os
import Pod
import Connection

env = os.environ.get("APP_ENV", "dev")
print(f"Starting application in {env} mode")

COUNT_OF_PODS = 5

def config_pods() -> array:
    return[ 
        Pod (f"http://localhost:{i}")
        for i in range(1,COUNT_OF_PODS)
    ]

class Balancier(Flask):
    _next = 0
    connections = []
    pods = config_pods()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def round_robin(self):
        for number in self.pods:
            pod = self.pods[number]
            if pod["is_active"]:
                #TODO send redirect 
                redirect()


app = Balancier(f"client")

# app.config.from_object(f"backend.{env}_settings")
app.server_id = 1

@app.route('/')
def hello_world():  # put application's code here
    print(app.round_robin())

if __name__ == '__main__':
    app.run()
