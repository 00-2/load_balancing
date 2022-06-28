from flask import Flask
import os

env = os.environ.get("APP_ENV", "dev")
print(f"Starting application in {env} mode")


class Client(Flask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



app = Client(f"client")

# app.config.from_object(f"backend.{env}_settings")
app.server_id = 1

@app.route('/')
def hello_world():  # put application's code here
    return str(app.server_id)

if __name__ == '__main__':
    app.run()
