from fastapi import FastAPI

app = FastAPI(title="RESTaurants")


@app.get("/")
async def healthcheck():
    return {"Status code": "200"}
