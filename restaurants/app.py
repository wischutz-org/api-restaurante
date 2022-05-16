from typing import List
from fastapi import FastAPI, HTTPException
from models import Restaurant

app = FastAPI(title="RESTaurants")

db: List[Restaurant] = [
    Restaurant(
        id=0,
        name="Sabores Secretos",
        neighborhood="Sumaré",
        address="R. José Erasmo de Moura, 100 - Alto do Sumaré, Mossoró - RN, 59633-680",
        cuisine_type="italian"
    ),
    Restaurant(
        id=1,
        name="Kiko Sushi",
        neighborhood="Doze Anos",
        address="Av. Diocesano, 2630 - Doze Anos, Mossoró - RN, 59603-200",
        cuisine_type="japanese"
    ),
    Restaurant(
        id=2,
        name="Yong Xiang",
        neighborhood="Centro",
        address="Av. Rio Branco, 2121 - Centro, Mossoró - RN, 59600-145",
        cuisine_type="chinese"
    )
]


@app.get("/")
async def healthcheck():
    return {"Status code": "200"}


@app.get("/restaurants")
async def fetch_restaurants():
    return db


@app.post("/restaurants")
async def register_restaurant(restaurant: Restaurant):
    db.append(restaurant)
    return {"id": restaurant.id}


@app.delete("/restaurants/{restaurant_id}")
async def delete_restaurant(restaurant_id: int):
    for restaurant in db:
        if restaurant.id == restaurant_id:
            db.remove(restaurant)
            return {"{restaurant_id}": "Deletado com sucesso!"}
    raise HTTPException(
        status_code=404,
        detail=f"restaurant with id: {restaurant_id} doesnt exists."
    )
