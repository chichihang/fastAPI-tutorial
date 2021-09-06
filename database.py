from model import User

import motor.motor_asyncio # MongoDB driver

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://dbHang:asdqwe123@hellodb.jso7j.mongodb.net/DataFromWebApp?retryWrites=true&w=majority')
# for connection of database.py and MongoDB

database = client.DataFromWebApp
collection = database.user


async def fetch_one_user(user_name: str):
    document = await collection.find_one({'user_name': user_name})
    return document

async def fetch_all_user():
    users = []
    cursor = collection.find({})
    async for document in cursor:
        users.append(User(**document))
    return users


async def create_user(user):
    document = user
    result = await collection.insert_one(document)
    return result


async def update_user(user_name: str, age: int):
    await collection.update_one(
        {'user_name': user_name},
        {'$set': {'age': age}})
    document = await collection.find_one({'user_name': user_name})
    return document


async def delete_user(user_name: str):
    await collection.delete_one({'user_name': user_name})
    return True

