from fastapi import FastAPI
import random
from faker import Faker

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def users():
    fake = Faker()
    num_rows = 1000
    users = []
    
    for i in range(num_rows):
        name = fake.name()
        city = fake.city()
        age = random.randint(18, 99)
        users.append({'name': name, 'city': city, 'age': age})
    return users
