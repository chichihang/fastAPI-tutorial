from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

#Fast API doc: https://fastapi.tiangolo.com/
#pydantic doc: https://pydantic-docs.helpmanual.io/

app = FastAPI()





class User(BaseModel):
    user_name: str
    age: int


class UpdateUser(BaseModel):
    user_name: Optional[str]
    age: Optional[int]


# Dataset sample
users = {
            0: {
                'user_name': 'Haha',
                'age': 26,
                }
        }


@app.get('/')
def index():
    return {'Testing': 'hello world'}

# Demo of Path parameters
@app.get('/get-user-by-id/{user_id}')
def path_params(user_id: int):
    return users[user_id]


# Demo of Query parameters
@app.get('/get-by-user-name')
def query_params(user_name: Optional[str]=None):
    for user_id in users:
        if users[user_id]['user_name'] == user_name:
            return users[user_id]
    return f'User: {user_name} not found'

@app.get('/this-is-combined-params-function/user_id={user_id}')
def get_user(*, user_id: int, user_name: str):
    if users[user_id]['user_name'] == user_name:
        return f'The selected user: {users[user_id]}'
    return 0


@app.post('/create-user/{user_id}')
def create_user(user_id: int, user: User):
    if user_id in users:
        return f'Cannot create user, user_id: {user_id} existed already'
    users[user_id] = user
    return users[user_id]


@app.put('/update-user')
def update_user(user_id: int, user: UpdateUser):
    if user_id in users:
        # For python 3.9.7: the key of dict can be called as a attribute
        # eg: dict.key == dict['key]
        if user.user_name != None:
            users[user_id]['user_name'] = user.user_name
        if user.age != None:
            users[user_id]['age'] = user.age

        users[user_id] = user
        return users[user_id]

    return {'Error': f'user_id: {user_id} not found'}


@app.delete('/delete-user')
def delete_user(user_id: int):
    if user_id not in users:
        return {'Error:': f'The user id:{user_id} does not exist.'}

    del users[user_id]
    return f'User-id: {user_id} is deleted'
"""
uvicorn: Since fast API is a very list library
        that require external lib to run the server

GET - gen an infomation
POST - create something new
PUT - update 
DELETE - delete something

Path parameters:
@app.get('/end-point/{path_parameters}')
def demo_path_parameters(path_parameters: dtype = Path(None, decription='haha'):
    #####
    return data
    
    
Query parameters:
@app.get('/end-point')
def demo_query_parameters(query_parameters: Optional[dtype]=None):
    #####
    return data
"""