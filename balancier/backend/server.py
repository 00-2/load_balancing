from flask import Flask, redirect
import os

env = os.environ.get("APP_ENV", "dev")
print(f"Starting application in {env} mode")


class Balancier(Flask):
    _next = 0
    connections = [{"SERVER_NAME", "реализовано ли соединение"}]
    pods = {
        "1":{"is_active":True},
        "2":{"is_active":True},
        "3":{"is_active":True}
    }
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
