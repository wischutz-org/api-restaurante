from flask import Flask

app = Flask(__name__)


msg = 'OK -- o status code é 200'


@app.get("/healthcheck")
def healthcheck():
    return "Ok! [Status Code: 200]"


app.run()
