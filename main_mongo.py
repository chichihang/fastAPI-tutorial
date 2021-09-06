from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel # helps to auto create JSON shcemas from the model
from fastapi.middleware.cors import CORSMiddleware
from model import User, UpdateUser
from database import fetch_one_user, fetch_all_user, create_user, update_user, delete_user
#Fast API doc: https://fastapi.tiangolo.com/
#pydantic doc: https://pydantic-docs.helpmanual.io/

app = FastAPI()


origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/mongo-test/fetch-all-user/')
async def get_user():
    response = await fetch_all_user()
    return response

@app.get('/mongo-test/get-by-user-name/}', response_model=User)
async def get_user_by_id(user_name: str):
    response = await fetch_one_user(user_name=user_name)
    if response:
        return response
    raise HTTPException(404, f'Cannot find user name: {user_name}')

@app.post('/mongo-test/create-user', response_model=User)
async def create_user_to_mongo(user: User):
    response = await create_user(user=user.dict())
    if response:
        return {'input data': response}
    raise HTTPException(400, 'Bad Request, try again')

@app.put('/mongo-test/update-user{user_name}/', response_model=User)
async def put_user(user_name: str, age: int):
    response = await update_user(user_name=user_name, age=age)
    if response:
        return response
    raise HTTPException(404, f'Cannot find user name: {user_name}')

@app.delete('/mongo-test/delete-user')
async def del_user(user_name: str):
    response = await delete_user(user_name=user_name)
    if response:
        return 'Deleted'
    raise HTTPException(404, f'Cannot find user name: {user_name}')